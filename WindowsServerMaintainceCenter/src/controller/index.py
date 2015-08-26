#!/usr/bin/env Python  
#coding=utf-8
'''
Created on Apr 13, 2015

@author: rogerlai
'''

import tornado.web

from common import process
from common.config import TEMPLATE_PATH, STATIC_HOST, WEB_SERVER_ADDR, ENV, \
    REMOTE_SERVERS


loader = tornado.web.template.Loader(TEMPLATE_PATH)

class WebGetIndexHandler(tornado.web.RequestHandler):      
    @staticmethod
    def get_handler(self):            
        param_dict = {}
        param_dict['title'] = u'%s Windows服务器管理系统' % ENV
        param_dict['static_host'] = STATIC_HOST
        param_dict['web_server'] = WEB_SERVER_ADDR
        param_dict['server_list'] = REMOTE_SERVERS
        
        server_type_list = []
        for server in REMOTE_SERVERS:
            if server.get('type') not in server_type_list:
                server_type_list.append(server.get('type')) 
        
        param_dict['server_type_list'] = server_type_list
        
        response = loader.load("index.html").generate(params = param_dict)                    
        return response
        
    def get(self):
        self.write(process.process_request(self.request, lambda: WebGetIndexHandler.get_handler(self), 'html')) 