import requests
def handler(event, context):

    print(event)

    try:
        # This is here to demonstrate the use of a dependency
        r = requests.get("https://www.amazon.com")
    except Exception as e:
        print(str(e))

