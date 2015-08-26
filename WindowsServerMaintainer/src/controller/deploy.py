'''
Created on Aug 9, 2015

@author: rogerlai
'''
import os
import shutil

import tornado.web
from subprocess import Popen, PIPE

from common import process, utils
from common.exceptions import StartDaemonProcessError


REMOTE_FOLDER = "C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Windows\\Network Shortcuts\\office_converter"
CONVERTER_FOLDER = 'C:\\windows-converter'
SCRIPT_FOLDER = 'C:\\WindowsServiceUpdate'

class RedeployHandler(tornado.web.RequestHandler):
    @staticmethod
    def get_handler(self):
        response = {}
        msg = ''
        
        # stop the service
        utils.kill_process_by_name('cmd.exe')
        utils.kill_process_by_name('java.exe')
        
        # update the code and config
        if os.path.exists('%s\\services-windows-converter-1.0-SNAPSHOT.jar' % CONVERTER_FOLDER):
            os.remove('%s\\services-windows-converter-1.0-SNAPSHOT.jar' % CONVERTER_FOLDER)
        
        if os.path.exists('%s\\conf\\application-config.xml' % CONVERTER_FOLDER):    
            os.remove('%s\\conf\\application-config.xml' % CONVERTER_FOLDER)
        
        if os.path.exists('%s\\lib' % CONVERTER_FOLDER):
            shutil.rmtree('%s\\lib' % CONVERTER_FOLDER)
        
#         shutil.copyfile('%s\\services-windows-converter-1.0-SNAPSHOT.jar' % REMOTE_FOLDER, '%s\\services-windows-converter-1.0-SNAPSHOT.jar' % CONVERTER_FOLDER)
#         shutil.copytree('%s\\conf' % REMOTE_FOLDER, '%s\\conf' % CONVERTER_FOLDER)
#         shutil.copytree('%s\\lib' % REMOTE_FOLDER, '%s\\lib' % CONVERTER_FOLDER)
#          
#         # unregister and register the dll 
#         result = os.system('C:\\Windows\\Microsoft.NET\\Framework64\\v4.0.30319\\RegAsm.exe -u C:\\OfficeConverter.dll')
#         if result != 0:
#             # failed to execute
#             raise UnregisterDLLError()
#          
#         os.remove('C:\\OfficeConverter.dll')
#          
#         shutil.copyfile('%s\OfficeConverter.dll' % REMOTE_FOLDER, 'C:\\OfficeConverter.dll')
#         result = os.system('C:\\Windows\\Microsoft.NET\\Framework64\\v4.0.30319\\RegAsm.exe C:\\OfficeConverter.dll /codebase')
#         if result != 0:
#             # failed to execute
#             raise RegisterDLLError()

        os.makedirs('%s\\lib' % CONVERTER_FOLDER)
        
        # run the batch file to update the service code and DLL
        p = Popen(['%s\\update.bat' % SCRIPT_FOLDER], stdout=PIPE, stderr=PIPE)
        output_msg = p.stdout.read()
        output_msg = output_msg.decode("gb2312")
        msg += unicode(output_msg.encode("utf-8"))
        
        # execute the bat to start the service and the daemon
        result = os.system('%s\\start.vbs' % SCRIPT_FOLDER)        
        if result != 0:
            # failed to execute
            raise StartDaemonProcessError()
        
        response['execute_message'] = msg
        return response
        
    def get(self):
        self.write(process.process_request(self.request, lambda: RedeployHandler.get_handler(self)))