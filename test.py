# -*- coding: utf8 -*-
import json

a = "打开学你说话"
b = "进入学你说话"

print(a == b)

if a == b or True :
    print("相等了")
else:
    print("不相等")
query = a.decode("utf-8")

speakText = query
if query == "打开学你说话".decode("utf-8") or query == "进入学你说话".decode("utf-8"):
    speakText = " "
response = {
    "version": "1.0",
    "is_session_end":False,
    "response": {
        "open_mic":True,
        "to_speak": {
            "type": 0,
            "text": speakText
        },
        "to_display": {
            "type": 0,
            "text": speakText
        }
    }
}

print(response)