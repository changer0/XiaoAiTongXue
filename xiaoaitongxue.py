# -*- coding: utf8 -*-

import sys
import json
import logging
print('Loading function')
logger = logging.getLogger()
def main_handler(event, context):
 logger.info("start main handler")
 print(event)
 
 body = json.loads(event['body'])
 query = body['query']
 print(query)

 responseBody = '这是一个测试，用来看看看能不能收到消息: ' + query
 response = {
     "is_session_end": False,
     "version": 1.0,
     "response" {
          "to_speak": {
            "type": 0,
            "text": "海浪的声音来咯"
        },
        "to_display": {
            "type": 0,
            "text": "海浪的声音来咯"
        },
     }

 }
 return response