#!/usr/bin/python3.6

import boto3
import sys

# Create SQS client
sqs = boto3.client('sqs')

def dequeue(queue_url):
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
    	WaitTimeSeconds=5
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
			dequeue(sys.argv[1])
		except KeyError:
			print('No messages on the queue!')
