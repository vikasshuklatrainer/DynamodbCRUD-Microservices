import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Students')

# Convert Decimal → int/float
def decimal_to_native(obj):
    if isinstance(obj, Decimal):
        return int(obj) if obj % 1 == 0 else float(obj)
    raise TypeError

def lambda_handler(event, context):
    print("EVENT:", event)

    body = None

    # Case 1: Body as string
    if isinstance(event.get("body"), str):
        body = json.loads(event["body"])

    # Case 2: Body already dict
    elif isinstance(event.get("body"), dict):
        body = event["body"]

    if not body:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Request body is required"})
        }

    # Validate input
    required_fields = ["studentId", "name", "age", "course"]
    for field in required_fields:
        if field not in body:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": f"{field} is required"})
            }

    response = table.update_item(
        Key={"studentId": body["studentId"]},
        UpdateExpression="SET #n = :name, age = :age, course = :course",
        ExpressionAttributeNames={
            "#n": "name"
        },
        ExpressionAttributeValues={
            ":name": body["name"],
            ":age": body["age"],
            ":course": body["course"]
        },
        ReturnValues="UPDATED_NEW"
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Student updated successfully",
            "updatedAttributes": response["Attributes"]
        }, default=decimal_to_native)
    }
