# -*- coding: utf8 -*-

import sys
import json
import logging

print('Loading function')
logger = logging.getLogger()


def main_handler(event, context):
    logger.info("start main handler")
    # print(event)

    body = json.loads(event['body'])
    query = body['query']
    print(query)

    speak_text = query
    if query == "打开学你说话".decode("utf-8") or query == "进入学你说话".decode("utf-8"):
        speak_text = " "  # 如果是启动语，不说话

    response = {
        "version": "1.0",
        "is_session_end": False,
        "response": {
            "open_mic": True,
            "to_speak": {
                "type": 0,
                "text": speak_text
            },
            "to_display": {
                "type": 0,
                "text": speak_text
            }
        }

    }
    return response
