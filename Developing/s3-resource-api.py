import boto3

s3     = boto3.resource('s3')
bucket = s3.Bucket('zenon-saavedra')

for object in bucket.objects.all():
	print(object)

s3.Bucket('zenon-saavedra').download_file('keys/zenonpub.asc', 'zenonpub.asc')
