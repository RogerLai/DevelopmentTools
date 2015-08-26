#!/usr/bin/env Python  
#coding=utf-8
'''
Created on Apr 13, 2015

@author: rogerlai
'''

import os

# where the service is deployed
SERVER_IP = '121.40.149.171'
ENV = u'测试环境'
WEB_SERVER_ADDR = 'http://121.40.149.171:8088'
STATIC_HOST = 'http://121.40.149.171/static'

HTTP_REQUEST_TIMEOUT_IN_SECONDS = 5

REMOTE_SERVERS = [{
                        'type': 'Office转换',
                        'url': 'http://172.16.2.130:8089/redeploy'
                    }]

#convert a relative path to absolute
def resolve_path(relative_path, absolute_path = None):
    # if absolute path wasn't specified, use current dir instead.
    if not absolute_path:
        absolute_path = os.path.abspath(os.path.dirname(__file__))
    
    while (relative_path.startswith('../')):
        absolute_path = os.path.dirname(absolute_path)
        relative_path = relative_path[3:] 

    if (not relative_path.startswith('/')):
        relative_path = '/' + relative_path

    return absolute_path + relative_path

TEMPLATE_PATH = resolve_path('../templates')