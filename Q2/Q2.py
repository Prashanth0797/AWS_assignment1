import boto3
import sys

bucket = sys.argv[0]
path = sys.argv[1]
key = path.split('/')[-1]
s3 = boto3.resource('s3')
versions = s3.Bucket(bucket).object_versions.filter(Prefix=key)
my_ver =[]
for version in versions:
    obj = version.get()
    print(obj.get('VersionId'), obj.get('ContentLength'), obj.get('LastModified'))
    my_ver.append(obj.get('VersionId'))

s3_client = boto3.client('s3')
s3.download_file(bucket, key, '/' + path, ExtraArgs={'VersionId':my_ver[1] })


