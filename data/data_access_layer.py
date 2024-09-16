import boto3
from botocore.exceptions import ClientError
from models.post_model import Post

TABLE_NAME = 'Posts'

dynamodb = boto3.resource('dynamodb', region_name="us-west-2", endpoint_url="http://localhost:8000")
table = dynamodb.Table(TABLE_NAME)

def save_post(post):
    try:
        table.put_item(
            Item={
                'id': post.id,
                'content': post.content,
                'sentiment': post.sentiment
            }
        )
    except ClientError as e:
        print(f"Unable to save post: {e}")
        return None
    return post

def fetch_all_posts():
    try:
        response = table.scan()
        posts = response.get('Items', [])
        return [Post(post['id'], post['content'], post['sentiment']) for post in posts]
    except ClientError as e:
        print(f"Unable to fetch posts: {e}")
        return []

def fetch_post(post_id):
    try:
        response = table.get_item(Key={'id': post_id})
        item = response.get('Item')
        if item:
            return Post(item['id'], item['content'], item['sentiment'])
        else:
            return None
    except ClientError as e:
        print(f"Unable to fetch post: {e}")
        return None

def update_post_in_db(post_id, updated_post):
    try:
        table.update_item(
            Key={'id': post_id},
            UpdateExpression="SET content = :content, sentiment = :sentiment",
            ExpressionAttributeValues={
                ':content': updated_post.content,
                ':sentiment': updated_post.sentiment
            }
        )
    except ClientError as e:
        print(f"Unable to update post: {e}")
        return None
    return updated_post

def delete_post_from_db(post_id):
    try:
        table.delete_item(Key={'id': post_id})
    except ClientError as e:
        print(f"Unable to delete post: {e}")
        return None
    return True