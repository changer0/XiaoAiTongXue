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

 response = {
     "version": "1.0",
     "is_session_end":False,
     "response": {
        "open_mic":True,
        "to_speak": {
            "type": 0,
            "text": query
        },
        "to_display": {
            "type": 0,
            "text": query
        }
     }

 }
 return response