"""
All API actions possible with cook model is defined here

"""

from api.v1.resources import app_bp
from flask import abort, make_response, request, jsonify
from models.cooks import CooksModel


global_cook = CooksModel()


# Get all cooks
@app_bp.route('/cooks', methods=['GET'])
def get_cooks():
    """
    Retrive all cook objects from database

    """

    found_objs = global_cook.fetch()

    if not found_objs:
        abort(404, description="Does not exist")

    return found_objs


# Get cook by id
@app_bp.route('/cooks/<cook_id>', methods=['GET'])
def get_cookid(cook_id):
    """
    Get cook by Id

    Args:
        cook_id: id of cook to retirve
    """

    found_obj = global_cook.fetch(cook_id)

    if not found_obj:
        abort(404, description="Does not exist")

    return found_obj


# Create a new cook
@app_bp.route('/cooks', methods=['POST'])
def create_cook():
    """
    create a new cook object

    """

    strict_args = ['name', 'password', 'domain']

    if not request.get_json():
        abort(400, description="Invalid input format. Input format must be json serialiazable")

    data = request.get_json()

    for name in strict_args:
        if name not in data:
            abort(400, description="'name', 'password' and 'domain' fields are mandatory")

    new_cook = CooksModel()

    new_cook.setUser(data['name'], data['password'])
    new_cook.setStatus(data.get('bio'), **data['domain'])

    new_cook.user_age = data.get('age')
    new_cook.user_gender = data.get('gender')
    new_cook.user_location = data.get('location')
    new_cook.user_contact['phone'] = data.get('phone')
    new_cook.user_contact['whatsappNum'] = data.get('whatsapp')
    new_cook.user_contact['email'] = data.get('email')

    stats = new_cook.save(True)

    if stats:
        return make_response(new_cook.usrInfo(), 201)
    

# Update a cook
@app_bp.route('/cooks/<cook_id>', methods=['PUT'])
def update_cook(cook_id):
    """
    Update a cook object in database

    """

    found_obj = global_cook.fetch(cook_id)

    if not found_obj:
        abort(404, description="Does not exist")

    if not request.get_json():
        abort(400, description="Invalid input format. Input must be json serializable")

    data = request.get_json()
    update = CooksModel(**found_obj) # Recreate object from dict representation

    usr = update.getUser()
    usr_bio = update.bio
    usr_sp = update.specialty

    for name in data:
        if name == "name":
           update.setUser(data['name'], usr['UserPasswd'])
        if name == "password":
            update.setUser(usr['UserName'], data['password'])
        if name == "bio":
            update.setStatus(data.get('bio'), **usr_sp)
        if name == "domain":
            update.setStatus(usr_bio, **data['domain'])
        if name == "age":
            update.user_age = data.get('age')
        if name == "gender":
            update.user_gender = data.get('gender')
        if name == "location":
            update.user_location = data.get('location')
        if name == "phone":
            update.user_contact['phone'] = data.get('phone')
        if name == "whatsapp":
            update.user_contact['whatsappNum'] = data.get('whatsapp')
        if name == "email":
            update.user_contact['email'] = data.get('email')

    stats = update.update()

    if stats:
        return make_response(update.usrInfo(), 200)


# Delete a cook
@app_bp.route('/cooks/<cook_id>', methods=['DELETE'])
def delete_cook(cook_id):
    """
    Remove cook object from database

    """

    found_obj = global_cook.fetch(cook_id)

    if not found_obj:
        abort(404, description="Does not exist")

    ins = CooksModel(**found_obj)

    stats = ins.destroy()

    if stats:
        return make_response(jsonify({"status": "DELETED"}), 200)