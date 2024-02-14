"""
Post model API logic is defined in this module

"""

from api.v1.resources import app_bp
from flask import abort, request, make_response, jsonify
from models.posts import PostModel
from models.cooks import CooksModel


global_post = PostModel()
global_cook = CooksModel()

# Get all posts
@app_bp.route('/posts', methods=['GET'])
def get_post():
    """
    Retrive all post from database

    """

    found_objs = global_post.fetch()

    if not found_objs:
        abort(404, description="Currently empty")

    return found_objs


# Get a post by id
@app_bp.route('/posts/<post_id>', methods=['GET'])
def get_postid(post_id):
    """
    Retrives a post basesd on post id

    Args"
        post_id
    """

    post = global_post.fetch(post_id)

    if not post:
        abort(404, description="Does not exist")

    return post


# Create a new post
@app_bp.route('/cooks/post/<cook_id>', methods=['POST'])
def create_post(cook_id):
    """
    Create a post for a cook

    Args:
        cook_id (str): id of cook who is making the post
    """

    strict_args = ['title', 'content']

    found_cook = global_cook.fetch(cook_id)

    if not found_cook:
        abort(404, description="The cook specified does not exist")
    
    if not request.get_json():
        abort(400, description="Invalid input format. Input values must be json serializable")

    cook = CooksModel(**found_cook)
    data = request.get_json()

    for name in strict_args:
        if name not in data:
            abort(400, description="'title' and 'content' fields are mandatory")

    post_title = data['title']
    post_text = data['content']
    post_media = data.get('media')

    stats = cook.createPost(post_title, post_text, post_media)

    if stats:
        return make_response(jsonify(cook.recentPost_info), 201)
    

# Update a post
@app_bp.route('/posts/<post_id>', methods=['PUT'])
def update_post(post_id):
    """
    update a post

    Args:
        post_id (str): id of post to update
    """

    found_obj = global_post.fetch(post_id)

    if not found_obj:
        abort(404, description="Does not exist")

    if not request.get_json():
        abort(400, description="Invalid input. Input must be json serializable")

    post = PostModel(**found_obj)
    data = request.get_json()

    for name in data:
        if name == "title":
            post.post_title = data.get('title')
        if name == "text":
            post.content['text'] = data.get('text')
        if name == "media":
            post.content['media'] = data.get('media')

    stats = post.update()

    if stats:
        return make_response(jsonify(post.dictify()), 200)
    

# Delete a post
@app_bp.route('/posts/<post_id>', methods=['DELETE'])
def delete_post(post_id):
    """
    Delete a post

    Args:
        post_id (str): id of post to delete
    """

    found_obj = global_post.fetch(post_id)

    if not found_obj:
        abort(404, description="Does not exist")

    post = PostModel(**found_obj)

    stats = post.destroy()

    if stats:
        return make_response(jsonify({'status': "DELETED"}))    


# Get all post of a specific user
@app_bp.route('/cooks/post/<cook_id>', methods=['GET'])
def get_cookPosts(cook_id):
    """
    Get all post by a particular cook

    Args:
        cook_id (str): id of the cook who's posts is to be retrived
    """

    found_objs = global_post.fetch_many(cook_id, "author.id")

    if not found_objs:
        abort(404, description="Does not exist")

    return found_objs