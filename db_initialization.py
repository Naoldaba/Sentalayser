import boto3
from botocore.exceptions import ClientError

TABLE_NAME = "Posts"
dynamodb = boto3.resource('dynamodb', region_name="us-west-2", endpoint_url="http://localhost:8000")

def create_posts_table():
    try:
        table = dynamodb.Table(TABLE_NAME)
        table.load()  
        print("Table already exists.")
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            table = dynamodb.create_table(
                TableName=TABLE_NAME,
                KeySchema=[
                    {
                        'AttributeName': 'id',
                        'KeyType': 'HASH'  
                    }
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'id',
                        'AttributeType': 'S'  
                    }
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            )
            table.wait_until_exists()
            print("Table created successfully.")
        else:
            print("Unexpected error occurred:", e)

create_posts_table()
