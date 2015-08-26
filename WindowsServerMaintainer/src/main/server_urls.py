'''
Created on Jun 19, 2013

@author: roger
'''

from controller import *

urls = [
        (r"/test", TestHandler),
        (r"/redeploy", RedeployHandler),
        ]