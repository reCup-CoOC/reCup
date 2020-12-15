# -*- coding: utf-8 -*-
import serial
import time
import threading
from servo_moteur_distribution import liberer_tasse_distribution 
serialPort = "/dev/ttyACM0"
baudRate = 115200
   
    
    
    
def init_machine():
    #paramètres
    ser = serial.Serial(serialPort, baudRate, timeout=0, writeTimeout=0)
    time.sleep(2)
 

    # autohome -> wait for "ok"
    ser.write(bytes("$H" + '\n', 'utf-8'))
    time.sleep(2)
    data =" "
    while True:
        data = ser.readline(1000).decode(encoding="UTF-8")
        if data == 'ok\r\n':
            break
    
    #déblocage machine 
    ser.write(bytes("$X" + '\n', 'utf-8'))
    time.sleep(2)
    data =" "
    while True:
        data = ser.readline(1000).decode(encoding="UTF-8")
        if data == 'ok\r\n':
            break
                  
    #position attente tasse
    ser.write(bytes("X227" + '\n', 'utf-8'))
    time.sleep(2)
    data =" "
    while True:
        data = ser.readline(1000).decode(encoding="UTF-8")
        if data == 'ok\r\n':
            break
     
    #sleep 
    ser.write(bytes("$SLP" + '\n', 'utf-8'))
    data =" "
    while True:
        data = ser.readline(1000).decode(encoding="UTF-8")
        ser.write(bytes("$SLP" + '\n', 'utf-8'))
        if data == '[MSG:Sleeping]\r\n':
            break
        time.sleep(1)

    




 
    

def servo():
    #TODO
    #ouverture 
    #fermeture
    time.sleep(4)
    liberer_tasse_distribution()

   
def carry_tasse(x,z):
    #détermnination position ou emmener la tasse
    position = "X"+str(x)+"Z"+str(z)
    
    
    #paramètres
    ser = serial.Serial(serialPort, baudRate, timeout=0, writeTimeout=0)
    time.sleep(2)
    #déplacement vers la postion

    # déblocage
    ser.write(bytes("$X" + '\n', 'utf-8'))
    time.sleep(2)
    data =" "
    while True:
        data = ser.readline(1000).decode(encoding="UTF-8")
        if data == 'ok\r\n':
            break
    
    #Position tasse
    ser.write(bytes(position + '\n', 'utf-8'))
    time.sleep(2)
    data =" "
    while True:
        data = ser.readline(1000).decode(encoding="UTF-8")
        if data == 'ok\r\n':
            break

    
    #ouverture/fermeture servo
    servo()

    
    #déplacement vers l'origine et extinction des moteurs (veille)
    #retourposition attente tasse
    ser.write(bytes("X0Z0" + '\n', 'utf-8'))
    time.sleep(2)
    data =" "
    while True:
        data = ser.readline(1000).decode(encoding="UTF-8")
        if data == 'ok\r\n':
            break
        
    #sleep
    ser.write(bytes("$SLP" + '\n', 'utf-8'))
    data =" "
    while True:
        data = ser.readline(1000).decode(encoding="UTF-8")
        ser.write(bytes("$SLP" + '\n', 'utf-8'))
        if data == '[MSG:Sleeping]\r\n':
            break
        time.sleep(1)  
    

#init_machine()
# carry_tasse(10,50)