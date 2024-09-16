from data.data_access_layer import save_post, fetch_all_posts, fetch_post, update_post_in_db, delete_post_from_db
from AI_service.sentiment_service import analyze_sentiment
from models.post_model import Post
import uuid

def create_new_post(content):
    post_id = str(uuid.uuid4())
    sentiment = analyze_sentiment(content)
    post = Post(post_id, content, sentiment)
    save_post(post)
    return post

def get_posts():
    return fetch_all_posts()

def get_single_post(post_id):
    return fetch_post(post_id)

def update_post(post_id, content):
    sentiment = analyze_sentiment(content)
    updated_post = Post(post_id, content, sentiment)
    update_post_in_db(post_id, updated_post)
    return updated_post

def delete_post(post_id):
    delete_post_from_db(post_id)
