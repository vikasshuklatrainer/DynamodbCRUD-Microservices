import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Students')

# Helper function to convert Decimal to int/float
def decimal_to_native(obj):
    if isinstance(obj, Decimal):
        return int(obj) if obj % 1 == 0 else float(obj)
    raise TypeError

def lambda_handler(event, context):
    student_id = event["queryStringParameters"]["studentId"]

    response = table.get_item(
        Key={
            "studentId": student_id
        }
    )

    item = response.get("Item")

    if not item:
        return {
            "statusCode": 404,
            "body": json.dumps({"message": "Student not found"})
        }

    return {
        "statusCode": 200,
        "body": json.dumps(item, default=decimal_to_native)
    }
