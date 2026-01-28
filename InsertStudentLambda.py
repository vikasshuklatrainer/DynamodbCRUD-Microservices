import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Students')

def lambda_handler(event, context):
    body = json.loads(event['body'])

    table.put_item(
        Item={
            "studentId": body["studentId"],
            "name": body["name"],
            "age": body["age"],
            "course": body["course"]
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Student inserted successfully"
        })
    }
