import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Students')

def decimal_to_native(obj):
    if isinstance(obj, Decimal):
        return int(obj) if obj % 1 == 0 else float(obj)
    raise TypeError

def lambda_handler(event, context):
    print("EVENT:", event)

    body = None

    # Case 1: From Function URL / API Gateway
    if isinstance(event.get("body"), str):
        body = json.loads(event["body"])

    # Case 2: From direct invocation
    elif isinstance(event.get("body"), dict):
        body = event["body"]

    # Case 3: Console plain JSON
    elif isinstance(event, dict):
        body = event

    if not body:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Request body is required"})
        }

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
        ExpressionAttributeNames={"#n": "name"},
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
