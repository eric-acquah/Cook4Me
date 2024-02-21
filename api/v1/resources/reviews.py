"""
This defines all the API actions that is possible with the review endpoint

"""

from api.v1.resources import app_bp
from models.reviews import ReviewModel
from flask import make_response, abort, jsonify, request


globalReview = ReviewModel()

# Get all reviews
@app_bp.route('/reviews', methods=['GET'])
def getReview():
    """
    Get all reviews from database

    """

    found_objs = globalReview.fetch()

    if not found_objs:
        abort(404, description="Currantly empty")

    return found_objs


# Get review by id
@app_bp.route('/reviews/<review_id>', methods=['GET'])
def getReviewId(review_id):
    """
    Get review by id

    """

    found_obj = globalReview.fetch(review_id)

    if not found_obj:
        abort(404, description="Does not exist")

    return found_obj


# Create a new review
@app_bp.route('/reviews/', methods=['POST'])
def createReview():
    """
    Creates a new review

    """

    strict_args = ['name', 'email', 'review']

    if not request.get_json():
        abort(400, description="Invalid input. Input format must be json serializable")

    data = request.get_json()

    for name in strict_args:
        if name not in data:
            abort(400, description="name, email and review fields are mandatory")

    review = ReviewModel()

    review.revierName = data['name']
    review.revierEmail = data['email']
    review.review = data['review']

    stats = review.save(True)

    if stats:
        return make_response(jsonify(review.dictify()), 201)
    

# Update a review
@app_bp.route('/reviews/<review_id>', methods=['DELETE'])
def deleteReview(review_id):
    """
    Deletes a review from database

    """

    found_obj = globalReview.fetch(review_id)

    if not found_obj:
        abort(404, description="Does not exist")

    review = ReviewModel(**found_obj)

    stats = review.destroy()

    if stats:
        return make_response(jsonify({'status': 'DELETED'}), 200)
 