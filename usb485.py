# -*- coding:utf-8 -*-
import serial
import minimalmodbus

conn=minimalmodbus.Instrument('COM6',1)
conn.serial.baudrate=9600
conn.serial.bytesize=8
conn.serial.parity=serial.PARITY_NONE
conn.serial.stopbits=1
conn.serial.timeout=0.1
conn.mode=minimalmodbus.MODE_ASCII
#conn.address=33
#conn.write_register(1,0,1,16,signed=False)
#registeraddress, value, numberOfDecimals=0, functioncode=16, signed=False

def get_RH():
    conn.address=97
    rh_a=conn.read_register(2,3,4,signed=False)
    rh=calcFromA(100,0,rh_a)
    return rh

def get_T():
    conn.address=97
    temp_a=conn.read_register(0,3,4,signed=False)
    temp=calcFromA(50,0,temp_a)
    return temp

def get_T_soil():
    conn.address=97
    temp_a=conn.read_register(1,3,4,signed=False)
    temp_soil=calcFromA(50,0,temp_a)
    return temp_soil

def set_motor(off):
    conn.address=33
    conn.write_bit(1,off,15)
    #val=conn.write_bit(1,off,15)
    #return val

#Ampere use
def calcFromA(max,min,data):
    return ((max-min)/16)*(data-4)+min
#Current use
def calcFromV(max,min,data):
    return ((max-min)/10)*data+min
