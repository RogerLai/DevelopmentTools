'''
Created on Aug 9, 2015

@author: rogerlai
'''
import json
import urllib2

from common.config import REMOTE_SERVERS, HTTP_REQUEST_TIMEOUT_IN_SECONDS


def do_redeploy():
    result = {}
    result['execute_results'] = [] 
    
    for server in REMOTE_SERVERS:
        info = {}
        try:        
            info = json.load(urllib2.urlopen(server['url'], timeout=HTTP_REQUEST_TIMEOUT_IN_SECONDS))            
        except Exception as e:
            # if the server is unreachable
            info['status_code'] = 2
            info['execute_message'] = e
        finally:
            info['url'] = server['url']
            info['type'] = server['type']
            result['execute_results'].append(info)
            
    
    return result