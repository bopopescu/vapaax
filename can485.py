# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import serial
import minimalmodbus
from threading import Thread,Lock
import time

# AI /AO /DI /DO set
ai = {'T':0 ,'RH':2 ,'Soil':1}
do = [1]

EN_485 =  4
GPIO.setmode(GPIO.BCM)
GPIO.setup(EN_485,GPIO.OUT)
GPIO.output(EN_485,GPIO.HIGH)

conn=minimalmodbus.Instrument('/dev/ttyS0',0)
conn.serial.baudrate=9600
conn.serial.bytesize=8
conn.serial.parity=serial.PARITY_NONE
conn.serial.stopbits=1
conn.serial.timeout=1
conn.mode=minimalmodbus.MODE_ASCII
#conn.debug=True
#conn.address=33
#conn.write_register(1,0,1,16,signed=False)
#registeraddress, value, numberOfDecimals=0, functioncode=16, signed=False
flag=0

def chack_flag(flag):
    if flag!=0:
        time.sleep(0.3)
        flag=0
    else:
        time.sleep(0.3)
        flag=1

def get_RH():
    chack_flag(0)
    conn.address=97
    rh_a=conn.read_register(ai['RH'],3,4,signed=False)
    rh=calcFromA(100,0,rh_a)
    return rh

def get_T():
    chack_flag(0)
    conn.address=97
    temp_a=conn.read_register(ai['T'],3,4,signed=False)
    temp=calcFromA(50,0,temp_a)
    return temp

def get_T_soil():
    chack_flag(0)
    conn.address=97
    temp_a=conn.read_register(ai['Soil'],3,4,signed=False)
    temp_soil=calcFromA(50,0,temp_a)
    return temp_soil

def set_motor(off):
    chack_flag(1)
    conn.address=33
    conn.write_bit(do[0],off,15)
    #val=conn.write_bit(1,off,15)
    #return val

#Ampere use
def calcFromA(max,min,data):
    return ((max-min)/16)*(data-4)+min
#Current use
def calcFromV(max,min,data):
    return ((max-min)/10)*data+min
