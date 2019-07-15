import boto3
rds_client = boto3.client('rds', region_name="us-east-1")


try:
 response = rds_client.create_db_instance(
 DBInstanceIdentifier='myserver',
 MasterUsername='admin_user',
 MasterUserPassword='qwert%E',
 DBInstanceClass='db.t2.micro',
 Engine='postgres',
 AllocatedStorage=5)
 print(response)
except Exception as error:
 print(error)


