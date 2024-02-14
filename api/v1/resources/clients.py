"""
This module defines all api actions that can be performed
on the client class

"""

from api.v1.resources import app_bp
from models.clients import ClientModel
from flask import request, make_response, abort, jsonify


client = ClientModel()


# Get all clients
@app_bp.route('/clients', methods=['GET'])
def get_clients():
    """
    Retrives all client objects from database

    """

    docs = client.fetch()

    return docs


# Get a client by id 
@app_bp.route('/clients/<client_id>', methods=['GET'])
def get_clientid(client_id):
    """
    Get a specific client object

    Args:
        client_id (str): id of the client object to retrive
    """

    found_obj = client.fetch(client_id)

    if not found_obj:
        abort(404)
    
    return found_obj


# Create a new client
@app_bp.route('/clients', methods=['POST'])
def create_client():
    """
    Create a new client object

    """

    strict_args = ['name', 'password']

    if not request.get_json():
        abort(400, description="Invalid input format. Input must be json serializable")

    for arg in strict_args:
        if arg not in request.get_json():
            abort(400, description="'name' and 'password' fields are mandatory")

    client_data = request.get_json()
    new_client = ClientModel()

    new_client.setUser(client_data['name'], client_data['password'])

    new_client.user_age = client_data.get('age')
    new_client.user_location = client_data.get('location')
    new_client.user_gender = client_data.get('gender')

    new_client.user_contact['phone'] = client_data.get('phone')
    new_client.user_contact['whatsappNum'] = client_data.get('whatsapp')
    new_client.user_contact['email'] = client_data.get('email')

    if new_client.save(True):
        return make_response(new_client.usrInfo(), 201)
    

# Update a client
@app_bp.route('/clients/<client_id>', methods=['PUT'])
def upadate_client(client_id):
    """
    Update an object in database

    Args:
        client_id (str): id of the object to update
    """

    if not request.get_json():
        abort(400, description="Invalid input format. Input must be json serializable")

    data = request.get_json()

    # Retrive object from database
    obj = client.fetch(client_id)

    if not obj:
        abort(404, description="Does not exist")

    update = ClientModel(**obj)

    usr = update.getUser()

    for name in data:
        if name == "name":
            update.setUser(data.get('name'), usr.get('UserPasswd'))
        if name == "password":
            update.setUser(usr.get('UserName'), data.get('password'))
        if name == "age":
            update.user_age = data.get('age')
        if name == "location":
            update.user_location = data.get('location')
        if name == "gender":
            update.user_gender = data.get('gender')
        
        if name == 'phone':
            update.user_contact['phone'] = data.get('phone')
        if name == "whatsapp":
            update.user_contact['whatsappNum'] = data.get('whatsapp')
        if name == "email":
            update.user_contact['email'] = data.get('email')

    if update.update():
        return make_response(update.usrInfo(), 200)
    

# Delete a client
@app_bp.route('/clients/<client_id>', methods=['DELETE'])
def delete_client(client_id):
    """
    Remove client object from database

    """

    obj = client.fetch(client_id)

    if not obj:
        abort(404, description="Does not exist")

    target = ClientModel(**obj)

    stats = target.destroy()

    if stats:
        return make_response(jsonify({'status': 'DELETED'}), 200)    