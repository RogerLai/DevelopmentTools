'''
Created on Jun 19, 2013

@author: roger
'''

from controller import *

urls = [
        (r"/", WebGetIndexHandler),
        (r"/redeploy", RedeployHandler),
        ]