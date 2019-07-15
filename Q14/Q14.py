import boto3

sqs = boto3.client('sqs')

queue_url = 'https://sqs.us-east-1.amazonaws.com/488599217855/prashanthQ13'

# Receive message from SQS queue
response = sqs.receive_message(
    QueueUrl=queue_url,
    AttributeNames=[
        'SentTimestamp'
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=0,
    WaitTimeSeconds=0
)

msg = response['Messages'][0]


src = msg[0]
source_key = msg[1]
dest_key = msg[2]

buckets_copy = {'Bucket': 'src', 'Key': 'src'}
copy(buckets_copy, src, dest_key)

sqs.delete_message(
    QueueUrl=queue_url,
    ReceiptHandle=receipt_handle
)
