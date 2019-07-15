import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb', region_name = 'us-west-2')

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='Games1',
    KeySchema=[
        {
            'AttributeName': 'gname',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'gid',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'gname',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'gid',
            'AttributeType': 'N'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

table.meta.client.get_waiter('table_exists').wait(TableName='Games1')
print(table.item_count)#To know if the table was creted succesfully

table.put_item(
    Item = {
        'gid': 1,
        'gname': 'Football',
        'publisher': 'Doe',
        'rating': 4,
        'genres': 'sports',
    }
)

table.meta.client.get_waiter('table_exists').wait(TableName='Games1')
print(table.item_count)#To know if the table was creted succesfully
