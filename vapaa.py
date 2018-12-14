# -*- coding:utf-8 -*-
import serial
import minimalmodbus
import time

def chack_flag(flag):
    if flag!=0:
        time.sleep(0.3)
        flag=0
    else:
        time.sleep(0.3)
        flag=1

def calcFromA(max,min,data):
    return ((max-min)/16)*(data-4)+min

def calcFromV(max,min,data):
    return ((max-min)/10)*data+min

class conn():
 def __init__(self, com):
  flag=0
  conn=minimalmodbus.Instrument(com,1)
  conn.serial.baudrate=9600
  conn.serial.bytesize=8
  conn.serial.parity=serial.PARITY_NONE
  conn.serial.stopbits=1
  conn.serial.timeout=0.4 # seconds. At least 0.2 seconds required for 2400 bits/s.
  conn.mode=minimalmodbus.MODE_ASCII

 def ai(self, id, type):
     chack_flag(0)
     conn.address=97
     data=conn.read_register(id,3,4,signed=False)
     #data=12.56
     if type=='T':
         return calcFromA(50, 0, data)
     elif type=='RH':
         return calcFromA(100, 0, data)
     elif type=='soil':
         return calcFromA(100, 0, data)

 def do(self, id, on):
     chack_flag(1)
     conn.address=33
     conn.write_bit(id, on, 15)
