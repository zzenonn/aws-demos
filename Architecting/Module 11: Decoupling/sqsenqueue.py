#!/usr/bin/python3.6

from time import sleep

import boto3
import sys

# Create SQS client
sqs = boto3.client('sqs')


def enqueue(queue_url, counter):
	sleep(5)
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
		enqueue(sys.argv[1], counter)
		counter = counter + 1
		print("Enqueuing Week " + str(counter))
