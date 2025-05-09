import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')

def lambda_handler(event, context):
    for record in event['Records']:
        try:
            order = json.loads(record['body'])
            table.put_item(Item=order)
            print(f"Order inserted: {order}")
        except Exception as e:
            print(f"Error: {e}")
    return {
        "statusCode": 200,
        "body": "Orders processed"
    }
