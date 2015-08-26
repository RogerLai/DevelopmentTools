'''
Created on Aug 9, 2015

@author: rogerlai
'''
import tornado.web

from common import process
from common.config import TEMPLATE_PATH
from model import redeploy_windows_service


loader = tornado.web.template.Loader(TEMPLATE_PATH)

class RedeployHandler(tornado.web.RequestHandler):
    @staticmethod
    def get_handler(self):
        param_dict = redeploy_windows_service.do_redeploy()
        
        response = loader.load("redeploy_result.html").generate(params = param_dict)                    
        return response
        
    def get(self):
        self.write(process.process_request(self.request, lambda: RedeployHandler.get_handler(self), 'html'))