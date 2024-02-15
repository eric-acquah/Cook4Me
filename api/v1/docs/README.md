By Eric Acquah <email: ericacquah1720@gmail.com>


#######
  API 
#######

These are the various endpoints of this application's API and some
opperations that can be done on each endpoint.
##################################################################

* For clients:

READ:
    /api/v1/clients => Get all clients objects - methods=[GET]
    /api/v1/clients/clientid => Get a client object by id
    /api/v1/clients/order/<UserId> => Get all orders by a particular user


CREATE:
    /api/v1/clients - methods=[POST] {
        'name': <username>, (mandatory field)
        'password': <userpassword>, (mandatory field)
        'age': <userage>,
        'gender': <usergender>,
        'location': <userlocation>,
        'phone': <userphonenumber>,
        'whatsapp': <userwhatsappnumber>,
        'email': <useremail>

    } => Creates and saves a new `client` user object with these attributes set for that object.


UPDATE:
    /api/v1/clients/<client_id> - methods=[PUT] {
        'name': <username>,
        'password': <userpassword>,
        'age': <userage>,
        'gender': <usergender>,
        'location': <userlocation>,
        'phone': <userphonenumber>,
        'whatsapp': <userwhatsappnumber>,
        'email': <useremail>

    } => updates and saves a `client` user object with these attributes set for that object.


DELETE:
    /api/v1/clients/<client_id> - methods=[DELETE] => Delete a `client` object from database




* For cooks:

READ:
    /api/v1/cooks => Get all cooks objects - methods=[GET]
    /api/v1/cooks/cookid => Get a cook object by id
    /api/v1/cooks/order/<UserId> => Get all orders by a particular cook
    /api/v1/cooks/post/<UserId> => Get all post by a particular cook


CREATE:
    /api/v1/cooks - methods=[POST] {
        'name': <username>, (mandatory field)
        'password': <userpassword>, (mandatory field)
        'age': <userage>,
        'gender': <usergender>,
        'location': <userlocation>,
        'phone': <userphonenumber>,
        'whatsapp': <userwhatsappnumber>,
        'email': <useremail>,
        'bio': <userbio> (short description of the cook),

        'domain': (mandatory field) {

            'cuisine': ["global", "regional", "dietary"],
            'dish': ["appetizers_and_snacks", "main_courses", "sides_and_soups", "desserts", "baking"],
            'cooking_style': ["classic", "modern", "healthy", "street_food"]

        } => (must be a selection of one or more subcategory in every category)

    } => Creates and saves a new `cook` user object with these attributes set for that object.


UPDATE:
    /api/v1/cooks/<cook_id> - methods=[PUT] {
        'name': <username>,
        'password': <userpassword>,
        'age': <userage>,
        'gender': <usergender>,
        'location': <userlocation>,
        'phone': <userphonenumber>,
        'whatsapp': <userwhatsappnumber>,
        'email': <useremail>
        'bio': <userbio> (short description of the cook),

        'domain': (mandatory field) {

            'cuisine': ["global", "regional", "dietary"],
            'dish': ["appetizers_and_snacks", "main_courses", "sides_and_soups", "desserts", "baking"],
            'cooking_style': ["classic", "modern", "healthy", "street_food"]

        } => (must be a selection of one or more subcategory in every category)

    } => updates and saves a `cook` user object with these attributes set for that object.


DELETE:
    /api/v1/cooks/<cook_id> - methods=[DELETE] => Delete a `cook` object from database




* For post:

READ:
    /api/v1/orders => Get all posts objects - methods=[GET]
    /api/v1/posts/postid => Get a post object by id


CREATE:
    /api/v1/posts/<cook_id> - methods=[POST] {
        'content': <textcontent>, (mandatory field)
        'head': <post_title>, (mandatory field)
        'media': <path_to_media_file>

    } => Creates and saves a new `post` object for a cook with these attributes set for that object.


UPDATE:
    /api/v1/posts/<post_id> - methods=[PUT] {
        'content': <textcontent>, (mandatory field)
        'head': <post_title>, (mandatory field)
        'media': <path_to_media_file>

    } => updates and saves a `client` user object with these attributes set for that object.


DELETE:
    /api/v1/posts/<post_id> - methods=[DELETE] => Delete a `client` object from database




* For order:

READ:
    /api/v1/orders => Get all orders objects - methods=[GET]
    /api/v1/orders/orderid => Get a order object by id


CREATE:
    /api/v1/orders - methods=[POST] {
        'clientid': <client_UserId>, (mandatory field)
        'cookid': <cook_UserId>, (mandatory field)
        'head': <order_head>, (mandatory field) (short description of the order)
        'description': <order_description> (detailed description of the order)

    } => Creates and saves a new `order` object for a cook with these attributes set for that object.


UPDATE:
    /api/v1/orders/<order_id> - methods=[PUT] {
        'clientid': <client_id>, (mandatory field)
        'cookid': <cook_id>, (mandatory field)
        'head': <order_head>, (mandatory field) (short description of the order)
        'description': <order_description> (detailed description of the order)

    } => updates and saves a `client` user object with these attributes set for that object.


DELETE:
    /api/v1/orders/<order_id> - methods=[DELETE] => Delete a `client` object from database
