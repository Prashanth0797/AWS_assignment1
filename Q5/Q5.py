import boto3
import json

def lamda_handler(event, context):
    s3_resource = boto3.resource('s3')
    dest_bucket_name = 'dest_bucket'
    source_bucket_name = 'source_bucket'
    flag = 0
    file_name = 'New Text file.txt'
    for key in s3_resource.list_objects(Bucket=source_bucket_name)['Contents']:
        files = key['Key']
        if(files == file_name):
            copy_source = {'Bucket': "source_bucket_name",'Key': files}
            s3_resource.meta.client.copy(copy_source, dest_bucket_name, files)
            flag = 1
            print(files)
            break
    if(flag == 0): #When the file is not found
        print('File not found')
