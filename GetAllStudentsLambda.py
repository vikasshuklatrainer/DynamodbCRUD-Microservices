import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Students')

# Convert Decimal to int/float
def decimal_to_native(obj):
    if isinstance(obj, Decimal):
        return int(obj) if obj % 1 == 0 else float(obj)
    raise TypeError

def lambda_handler(event, context):
    print("EVENT:", event)

    response = table.scan()
    items = response.get("Items", [])

    return {
        "statusCode": 200,
        "body": json.dumps(items, default=decimal_to_native)
    }
