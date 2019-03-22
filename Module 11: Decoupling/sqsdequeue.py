#!/usr/bin/python3.6

import boto3

# Create SQS client
sqs = boto3.client('sqs')

queue_url = 'https://sqs.ap-southeast-1.amazonaws.com/883779074323/TestQueue'

def dequeue():
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
    	VisibilityTimeout=30,
    	WaitTimeSeconds=0
	)

	message = response['Messages'][0]
	receipt_handle = message['ReceiptHandle']

	# Delete received message from queue
	sqs.delete_message(
    	QueueUrl=queue_url,
    	ReceiptHandle=receipt_handle
	)
	print('Received and deleted message: %s' % message)

if __name__ == "__main__":
	while(True):
		try:
			dequeue()
		except KeyError:
			print('No messages on the queue!')
