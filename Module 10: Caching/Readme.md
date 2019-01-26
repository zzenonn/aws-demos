# Caching with Cloudfront

## Create an S3 Bucket
1. Create an S3 bucket that should be made public. Use the following bucket policy
2. Upload the contents of the S3 folder to the S3 bucket

## Create a Cloudfront Distribution
1. Make sure Restrict bucket access is yes
2. Make cloudfront create a new access identity
3. Tell cloudfront to update the bucket policy
4. Make sure the default root object is set to cf_lab1.html
5. Show that the data is accessible via Cloudfront but not S3

**Note: Ideally, have a distribution already ready. Cloudfront distributions take a while to setup. I suggest running through these steps, but still having a finished one prepared.**