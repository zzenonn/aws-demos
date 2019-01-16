
# Transfer Acceleration
- Visit this site first http://s3-accelerate-speedtest.s3-accelerate.amazonaws.com/en/accelerate-speed-comparsion.html

# Hosting Static Website
## Steps to Take
1. Create an S3 bucket for static hosting (allow public access) and enable versioning
2. Upload the contents of the HTML folder to S3
3. Make the website publicly accessible. Use the following bucket policy
```
{
    "Version": "2012-10-17",
    "Id": "Policy1497053408897",
    "Statement": [
        {
            "Sid": "Stmt1497053406813",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::zenon-idw/*"
        }
    ]
}
```
4. Upload new index.html to showcase versioning
5. Delete latest to showcase revert