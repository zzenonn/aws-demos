# Launching a Web Server on EC2

## Steps:

1. Launch an EC2 Instance running Ubuntu 18.04 with the following Userdata
```
<html>
<body>
<h2>EC2 Instance Metadata</h2>
<a href="http://169.254.169.254/latest/meta-data/">Instance Metadata</a><BR/>
<a href="http://169.254.169.254/latest/meta-data/hostname">Instance Hostname</a><BR/>
<a href="http://169.254.169.254/latest/meta-data/public-ipv4">Instance Public IP Address</a><BR/>
<a href="http://169.254.169.254/latest/meta-data/placement/availability-zone">Instance Availability Zone</a><BR/>
<a href="http://169.254.169.254/latest/user-data">Instance User Data</a>
</body>
</html>
```
2. Security Groups should allow RDP (Remote Desktop Viewer), HTTP, and HTTPS.