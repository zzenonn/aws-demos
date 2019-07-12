# CLI Commands
This document lists a series of CLI commands for demonstration purposes.

## Creating a Key-pair

`aws ec2 create-key-pair --key-name test --output json --query "KeyMaterial"`

`aws ec2 create-key-pair --key-name test --output text --query "KeyMaterial"`

## Deleting a Key-pair

`aws ec2 delete-key-pair --key-name test --output json`

## Create VPC

`aws ec2 create-vpc --cidr-block 10.1.0.0/16 --output json`

## Delete VPC

`aws ec2 delete-vpc --vpc-id $(aws ec2 describe-vpcs --filter "Name=cidr-block,Values=10.1.0.0/16" --query "Vpcs[*].VpcId" --output text)`

## Describe VPC

`aws ec2 describe-vpcs --filter "Name=cidr-block,Values=172.31.0.0/16" --query "Vpcs[*].VpcId" --output text`

## Describe EC2 Instances

`aws ec2 describe-instances --filter "Name=tag:Name,Values=MongoDB"`

## Retrieve SSM Parameters

`aws ssm get-parameter --name /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2 --query Parameter.Value`
