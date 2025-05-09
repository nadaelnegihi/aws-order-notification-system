import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')

def lambda_handler(event, context):
    # Process each message from SQS
    for record in event['Records']:
        try:
            # Parse SQS message body (which comes from SNS)
            sns_message = json.loads(record['body'])
            order_data = json.loads(sns_message['Message'])
            
            # Validate required fields
            required_fields = ['orderId', 'userId', 'itemName', 'quantity', 'status', 'timestamp']
            if not all(field in order_data for field in required_fields):
                raise ValueError('Missing required fields in order data')
            
            # Write to DynamoDB
            response = table.put_item(
                Item={
                    'orderId': order_data['orderId'],
                    'userId': order_data['userId'],
                    'itemName': order_data['itemName'],
                    'quantity': order_data['quantity'],
                    'status': order_data['status'],
                    'timestamp': order_data['timestamp']
                }
            )
            
            # Log success
            print(f"Successfully processed order {order_data['orderId']}")
            print(f"DynamoDB response: {response}")
            
        except Exception as e:
            print(f"Error processing message: {str(e)}")
            raise e  # SQS will handle retries and DLQ
            
    return {
        'statusCode': 200,
        'body': json.dumps('Order processing complete')
    }
