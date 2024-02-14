"""
API actions for orders is defined in this module

"""

from api.v1.resources import app_bp
from flask import abort, request, make_response, jsonify
from models.orders import OrderModel
from models.clients import ClientModel
from models.cooks import CooksModel


global_order = OrderModel()
global_client = ClientModel()
global_cook = CooksModel()


# Get all orders
@app_bp.route('/orders', methods=['GET'])
def get_orders():
    """
    Retrive all order instances

    """

    found_objs = global_order.fetch()

    if not found_objs:
        abort(404, description="Does not exist")

    return found_objs


# Get an order by id
@app_bp.route('/orders/<order_id>', methods=['GET'])
def get_orderid(order_id):
    """
    Get order by id

    Args:
        order_id (str): id of order to to retrive
    """

    found_obj = global_order.fetch(order_id)

    if not found_obj:
        abort(404, description="Does not exist")

    return found_obj


# Create a new order
@app_bp.route('/orders', methods=['POST'])
def create_order():
    """
    Create a new order

    """

    strict_args = ['cookid', 'clientid', 'head']

    if not request.get_json():
        abort(400, description="Invalid input format. Input must be json serializable")

    data = request.get_json()

    for name in strict_args:
        if name not in data:
            abort(400, description="cookid, clientid and head fields are mandatory")

    found_cook = global_cook.fetch_many(data['cookid'], "_UserBase__user_credentials.UserId")
    found_client = global_client.fetch_many(data['clientid'], "_UserBase__user_credentials.UserId")

    if not found_cook:
        abort(404, description="The cook specified does not exist")
    if not found_client:
        abort(404, description="The client specified does not exist")

    client = ClientModel(**found_client[0])

    stats = client.makeOrder(data['cookid'], data['head'], data.get('description'))

    if stats:
        return make_response(client.recentOrder)


# Update an order
@app_bp.route('/orders/<order_id>', methods=['PUT'])
def update_order(order_id):
    """
    Update an order

    """

    found_obj = global_order.fetch(order_id)

    if not found_obj:
        abort(404, description="Does not exist")

    if not request.get_json():
        abort(400, description="Invalid input format. Input must be json serializable")

    data = request.get_json()
    order = OrderModel(**found_obj)

    for name in data:
        if name == "head":
            order.request['request_head'] = data.get('head')
        if name == "description":
            order.request['request_desc'] = data.get('description')
        if name == "cookid":
            order.cook_id = data.get('cookid')

    stats = order.update()

    if stats:
        return make_response(jsonify(order.dictify()), 200)
    

# Delete an order
@app_bp.route('/orders/<order_id>', methods=['DELETE'])
def delete_order(order_id):
    """
    Delete an order

    """

    found_obj = global_order.fetch(order_id)

    if not found_obj:
        abort(404, description="Does not exist")

    order = OrderModel(**found_obj)

    stats = order.destroy()

    if stats:
        return make_response(jsonify({'status': "DELETED"}), 200)
    

# Get all orders from a specific user
@app_bp.route('/clients/order/<client_id>', methods=['GET'])
def get_allClientOrders(client_id):
    """
    Get all orders from a specific client

    """

    found_obj = global_client.fetch(client_id)

    if not found_obj:
        abort(404, description="The client specified does not exist")

    client = ClientModel(**found_obj)

    usr = client.getUser()
    orders = global_order.fetch_many(usr['UserId'], 'client_id')

    if orders:
        return make_response(jsonify(orders), 200)
    

# Get all orders from a specific user
@app_bp.route('/cooks/order/<cook_id>', methods=['GET'])
def get_allCookOrders(cook_id):
    """
    Get all orders from a specific cook

    """

    found_obj = global_cook.fetch(cook_id)

    if not found_obj:
        abort(404, description="The cook specified does not exist")

    cook = CooksModel(**found_obj)

    usr = cook.getUser()
    orders = global_order.fetch_many(usr['UserId'], 'cook_id')

    if orders:
        return make_response(jsonify(orders), 200)