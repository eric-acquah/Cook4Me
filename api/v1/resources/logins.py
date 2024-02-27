"""
This defines the endpoints for user login details
 
"""

from api.v1.resources import app_bp
from flask import make_response, jsonify, abort, request
from models.logins import LoginModel


global_login = LoginModel()

# Get all logins
@app_bp.route('/logins', methods=['GET'])
def getLogin():
    """
    Retrieves all login objects

    """

    found_objs = global_login.fetch()

    if not found_objs:
        abort(404, description="Currently empty")

    return found_objs


# Get login object by Id
@app_bp.route('/logins/<login_id>', methods=['GET'])
def getLoginId(login_id):
    """
    Get a particular login object by it's Id

    """

    found_obj = global_login.fetch(login_id)

    if not found_obj:
        abort(404, description="Does not exist")

    return found_obj


# Create a new login object
@app_bp.route('/logins', methods=['POST'])
def createLogin():
    """
    Create a new login object

    """

    strict_args = ['name', 'password', 'id']

    if not request.get_json():
        abort(400, description="Invalid input. Input format must be json serializable")

    data = request.get_json()

    for name in strict_args:
        if name not in data:
            abort(400, description="Fields name, password and id are mandatory")

    login = LoginModel()

    login.usrIdentity['usrName'] = data['name']
    login.usrIdentity['usrPasswd'] = data['password']
    login.usrIdentity['usrObjId'] = data['id']

    stats = login.save(True)

    if stats:
        return make_response(jsonify(login.dictify()), 201)


# Update user login
@app_bp.route('/logins/<login_id>', methods=['PUT'])
def updateLogin(login_id):
    """
    Update the login object

    """

    found_obj = global_login.fetch(login_id)

    if not found_obj:
        abort(404, description="Does not exist")

    if not request.get_json():
        abort(400, description="Invalid input. Input must be json serializable")

    data = request.get_json()
    login = LoginModel(**found_obj)

    for name in data:
        if name == "name":
            login.usrIdentity['usrName'] = data.get('name')
        if name == "id":
            login.usrIdentity['usrObjId'] = data.get('id')
        if name == "password":
            login.usrIdentity['usrPasswd'] = data.get('password')

    stats = login.update()

    if stats:
        return make_response(jsonify(login.dictify()), 200)


# Delete a login object
@app_bp.route('/logins/<login_id>', methods=['DELETE'])
def deleteLogin(login_id):
    """
    Delete a login object

    """

    found_obj = global_login.fetch(login_id)

    if not found_obj:
        abort(404, description="Does not exist")

    login = LoginModel(**found_obj)

    stats = login.destroy()

    if stats:
        return make_response(jsonify({'status': "DELETED"}), 200)
    