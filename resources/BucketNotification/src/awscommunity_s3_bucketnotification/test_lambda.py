"Test lambda handler for config_integ"
import json

def handle(event, context):
    "Handler"
    print(event)
    print(context)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello World')
    }

