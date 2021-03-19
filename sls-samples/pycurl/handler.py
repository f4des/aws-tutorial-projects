import json
import requests


def hello(event, context):
    x = requests.get('https://qec1a4inl9.execute-api.us-east-1.amazonaws.com/dev')

    body = str(x.headers)




    response = {
        "statusCode": x.status_code,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
