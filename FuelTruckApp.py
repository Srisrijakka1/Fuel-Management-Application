import os
import boto3

def lambda_handler(event, context):
    # enter your sqs queue url to get the messages.
    QUEUE_URL = os.environ['queue_url']
    
    # sqs client
    client = boto3.client('sqs')
    
    receiveMessage = client.receive_message(
        QueueUrl=QUEUE_URL,
        MaxNumberOfMessages=10,
        WaitTimeSeconds=5
    )
    
    for m in receiveMessage.get('Messages', []):

        print("Fuel truck has been dispatched to gas station " + m['Body'] + ".")
        
        receipt_handle = m['ReceiptHandle']
        client.delete_message(
            QueueUrl=QUEUE_URL,
            ReceiptHandle=receipt_handle
        )
    
    processed_messages = len(receiveMessage.get('Messages', []))
    
    if processed_messages == 0:
        message = 'No messages found in queue. Messages processed: ' + str(processed_messages)
    else:
        message = 'Messages processed: ' + str(processed_messages)
        
    return message
