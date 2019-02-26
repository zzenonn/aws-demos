# IAM Roles

## IAM User
1. Show how your IAM user can assume an admin role despite having limited privelages

## EC2
1. Create an S3 readonly role (should already be created beforehand)
2. Create an EC2 instance with no role
3. Show that it currently has no access to S3 (`curl http://169.254.169.254/latest/meta-data/iam/security-credentials/`)
4. Attach S3 readonly role to EC2 instance
5. Show that you can now read S3 buckets
6. Run `curl http://169.254.169.254/latest/meta-data/iam/security-credentials/` to show credentials