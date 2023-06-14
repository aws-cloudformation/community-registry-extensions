import requests
def handler(event, context):

    print(event)

    try:
        # This is here to demonstrate the use of a dependency
        r = requests.get("https://www.amazon.com")

        # Add whatever compliance code you need here.
        
        # The event has the following properties:
        #
        # event["type_name"]             e.g. AWS::S3::Bucket
        # event["operation"]             create|update|delete
        # event["resource_properties"]   {}

    except Exception as e:
        print(str(e))

