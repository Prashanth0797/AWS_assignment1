import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

table = dynamodb.Table('Games1')
response = table.query(
    ProjectionExpression="gname, ratings",
    KeyConditionExpression = Key('gid').eq(2)
)

print(response)
