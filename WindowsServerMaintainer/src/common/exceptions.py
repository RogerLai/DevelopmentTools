#!/usr/bin/env Python  
#coding=utf-8
'''
Created on Jun 23, 2013

@author: roger
'''

class ErrorMessage:
    token_invalid_error = u'token失效'
    unregister_dll_error = u'注销DLL失败'
    register_dll_error = u'注册DLL失败'
    update_bat_execution_error = u'更新代码和DLL失败'
    start_daemon_error = u'启动守护进程失败'
    incorrect_json_format = u'不是有效的JSON格式'

class ServerError(Exception):
    # define basic emma exception
    def __init__(self, error_message):
        Exception.__init__(self, error_message)
        self.error_message = error_message

class TokenInvalidError(ServerError):
    def __init__(self, error_message = ErrorMessage.token_invalid_error):
        ServerError.__init__(self, error_message) 

class UnregisterDLLError(ServerError):
    def __init__(self, error_message = ErrorMessage.unregister_dll_error):
        ServerError.__init__(self, error_message) 
        
class RegisterDLLError(ServerError):
    def __init__(self, error_message = ErrorMessage.register_dll_error):
        ServerError.__init__(self, error_message)                               

class StartDaemonProcessError(ServerError):
    def __init__(self, error_message = ErrorMessage.register_dll_error):
        ServerError.__init__(self, error_message)    
        
class UpdateBatExecutionError(ServerError):
    def __init__(self, error_message = ErrorMessage.update_bat_execution_error):
        ServerError.__init__(self, error_message)                               
     
class IncorrectJsonObjError(ServerError):
    def __init__(self, error_message = ErrorMessage.incorrect_json_format):
        ServerError.__init__(self, error_message)