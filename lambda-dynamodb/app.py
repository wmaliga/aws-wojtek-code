import boto3
import json
import uuid

client = boto3.client('dynamodb')


def lambda_handler(event, context):
    if 'name' not in event:
        raise Exception('Name key is missing!')

    key = str(uuid.uuid1())
    name = event['name']

    client.put_item(
        TableName='DemoTable',
        Item={
            'id': {
                'S': key
            },
            'name': {
                'S': name
            }
        })

    return {
        'statusCode': 200,
        'body': json.dumps('Success! (ID = {})'.format(key))
    }
