import urllib3
import json
http = urllib3.PoolManager()


def lambda_handler(event, context):
    url = "https://hooks.slack.com/services/XXXXXXX/XXXXXXXXX/XXXXXXXXXXXXXXXXXXX"
    msg = {
        "channel": "#lambda",
        "username": "",
        "text": "Hello From Lambda",
        "icon_emoji": ""
    }

    encoded_msg = json.dumps(msg).encode('utf-8')
    resp = http.request('POST', url, body=encoded_msg)
    print({
        "message": "Hello From Lambda", 
        "status_code": resp.status, 
        "response": resp.data
    })