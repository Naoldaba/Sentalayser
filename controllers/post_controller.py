from flask import Blueprint, request, jsonify
from services.post_service import create_new_post, get_posts, get_single_post, update_post, delete_post

post_blueprint = Blueprint('post_controller', __name__)

@post_blueprint.route('/sentiments', methods=['POST'])
def create_post_route():
    data = request.json
    content = data.get('content')
    post = create_new_post(content)
    return jsonify(post.to_dict()), 201

@post_blueprint.route('/sentiments', methods=['GET'])
def get_posts_route():
    posts = get_posts()
    return jsonify([post.to_dict() for post in posts]), 200

@post_blueprint.route('/sentiments/<sentiment_id>', methods=['GET'])
def get_post_route(sentiment_id):
    post = get_single_post(sentiment_id)
    if not post:
        return jsonify({'message': 'Post not found'}), 404
    return jsonify(post.to_dict()), 200

@post_blueprint.route('/sentiments/<sentiment_id>', methods=['PUT'])
def update_post_route(sentiment_id):
    data = request.json
    content = data.get('content')
    updated_post = update_post(sentiment_id, content)
    return jsonify(updated_post.to_dict()), 200

@post_blueprint.route('/sentiments/<sentiment_id>', methods=['DELETE'])
def delete_post_route(sentiment_id):
    delete_post(sentiment_id)
    return jsonify({'message': 'Post deleted successfully'}), 200