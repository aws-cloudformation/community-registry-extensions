"Custom resource handler to sleep for SecondsToSleep seconds"

import json
import time
import traceback
import urllib3

http = urllib3.PoolManager()
SUCCESS = "SUCCESS"
FAILED = "FAILED"

def handler(event, context):
    "Lambda handler"
    responseData = {}
    try:
        print(event)
        time_to_wait = int(event['ResourceProperties']['SecondsToSleep'])
        print('wait started:',time_to_wait)
        time.sleep(time_to_wait)
        responseData['Data'] = "wait complete"
        print("wait completed")
    except Exception as e:
        print(traceback.format_exc())
        send(event, context, FAILED, responseData)

    send(event, context, SUCCESS, responseData)

def send(event, context, responseStatus, responseData, physicalResourceId=None, noEcho=False, reason=None):
    "Send the event"

    responseUrl = event['ResponseURL']

    print(responseUrl)

    responseBody = {
        'Status' : responseStatus,
        'Reason' : reason or "See the details in CloudWatch Log Stream: {}".format(context.log_stream_name),
        'PhysicalResourceId' : physicalResourceId or context.log_stream_name,
        'StackId' : event['StackId'],
        'RequestId' : event['RequestId'],
        'LogicalResourceId' : event['LogicalResourceId'],
        'NoEcho' : noEcho,
        'Data' : responseData
    }

    json_responseBody = json.dumps(responseBody)

    print("Response body:")
    print(json_responseBody)

    headers = {
        'content-type' : '',
        'content-length' : str(len(json_responseBody))
    }

    try:
        response = http.request('PUT', responseUrl, headers=headers, body=json_responseBody)
        print("Status code:", response.status)


    except Exception as e:

        print("send(..) failed executing http.request(..):", e)

