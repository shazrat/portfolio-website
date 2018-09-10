""" Simple Contact Form Emailer using AWS API Gateway, Lambda, and SES.
    Author: Shiraz Hazrat (shiraz@shirazhazrat.com)
    Version: 0.1
    
    Very crude implementation. Many updates to come.
    
"""


import boto3
import json
from urllib.parse import unquote

def respond(err, res=None):
    response = {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'text/html',
        }
    }
    return response

def send_email(name, email, message):
    subject = 'New message from shirazhazrat.com Contact Form!'
    body = 'Name: {}\n' \
            'Email: {}\n' \
            'Message: {}\n'.format(name, email, message)
    
    client = boto3.client('ses')
    response = client.send_email(
        Source='shiraz+contactform@shirazhazrat.com',
        Destination={
            'ToAddresses': ['shiraz@shirazhazrat.com']
        },
        Message={
            'Subject': {'Data': subject},
            'Body': {'Text': {'Data': body, 'Charset': 'UTF-8'}}
        }
    )

def lambda_handler(event, context):
    payload = unquote(event['body'])
    params = payload.split('&')
    name = params[0][5:]
    email = params[1][6:]
    message = params[2][8:]

    send_email(name, email, message)
    
    thank_you_message = "Thank you. I'll get back to you shortly! " \
                        "(I know this response page is dry. I'll add some style later...)"
    response = respond(None, thank_you_message)
    return response