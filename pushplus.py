import requests
import json
import os


def send_message(title, content):
# 不要用我的token(*´I`*)
    token = os.environ.get("PUSH_PLUS_TOKEN")
    url = "http://www.pushplus.plus/send"
    data = {"token": token, "title": title, "content": content, "template": 'markdown'}
    body = json.dumps(data).encode(encoding="utf-8")
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=body, headers=headers)
    return response.text
