import boto3

s3     = boto3.client('s3')
response = s3.list_objects(Bucket='zenon-saavedra')
print(response['Contents'])

