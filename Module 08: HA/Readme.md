# Autoscaling Demo

## Steps
1. Create a target group and load balancer to forward traffic to port 80
2. Create launch template.
    - MAKE SURE `Assign a public IP address to every instance.` IS TICKED
    - Use the following Userdata

```
#!/bin/bash -ex
yum -y update
yum -y install httpd php mysql php-mysql
chkconfig httpd on
sudo systemctl start httpd
if [ ! -f /var/www/html/lab2-app.tar.gz ]; then
cd /var/www/html
wget https://us-west-2-aws-training.s3.amazonaws.com/awsu-ilt/AWS-100-ESS/v4.2/lab-2-configure-website-datastore/scripts/lab2-app.tar.gz
tar xvfz lab2-app.tar.gz
chown apache:root /var/www/html/rds.conf.php
fi
```
3. Go to the load balancer's DNS address then load test.