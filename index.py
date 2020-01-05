# -*- coding: utf8 -*-

import sys
import logging
print('Loading function')
logger = logging.getLogger()
def main_handler(event, context):
 logger.info("start main handler")
 print(event)
 

 body = '这是一个测试，用来看看看能不能收到消息: '+event['body']
 response = {
     "isBase64": False,
     "statusCode": 200,
     "headers": {"Content-Type": "text", "Access-Control-Allow-Origin": "*"},
     "body": body
 }
 return response
