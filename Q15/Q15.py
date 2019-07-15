import json
import boto3
def lamda_handler(events, context):
    message = {"name": "prashanth"}
    client = boto3.client('sns')
    response = client.publish(
        TargetArn='arn:aws:sns:us-east-1:488599217855:Topic_1',
        Message=json.dumps({'default': json.dumps(message)}),
        MessageStructure='json')
