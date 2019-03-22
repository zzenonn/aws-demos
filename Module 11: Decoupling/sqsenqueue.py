#!/usr/bin/python3.6

from time import sleep

import boto3


# Create SQS client
sqs = boto3.client('sqs')

queue_url = 'https://sqs.ap-southeast-1.amazonaws.com/883779074323/TestQueue'

def enqueue(counter):
	sleep(2)
	# Send message to SQS queue
	response = sqs.send_message(
		QueueUrl=queue_url,
		DelaySeconds=0,
		MessageAttributes={
			'Title': {
				'DataType': 'String',
				'StringValue': 'The Whistler'
			},
			'Author': {
				'DataType': 'String',
				'StringValue': 'John Grisham'
			},
			'WeeksOn': {
				'DataType': 'Number',
				'StringValue': str(counter)
			}
		},
		MessageBody=(
			'Information about current NY Times fiction bestseller for '
			'week ' + str(counter)
		)
	)

	print(response['MessageId'])
	

if __name__ == "__main__":
	counter = 0
	while(True):
		enqueue(counter)
		counter = counter + 1
		print("Enqueuing Week " + str(counter))
