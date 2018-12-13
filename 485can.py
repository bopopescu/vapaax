# -*- coding:utf-8 -*-
import serial
import minimalmodbus

#Ampere use
def calcFromA(max,min,data):
    return ((max-min)/16)*(data-4)+min
#Current use
def calcFromV(max,min,data):
    return ((max-min)/10)*data+min

def get_T():
    temp=usb485(97,'T')
    return (temp)

def get_RH():
    rh=23
    return(tec)

def get_T_soil():
    temp=32
    return (temp)

def set_motor(off):
    #485usb(33)
    #off=0
    return conn.write_bit(1,off,15)

def usb485(address,type):
    try:
    	conn=minimalmodbus.Instrument('/dev/ttyS0',0)
    	conn.serial.baudrate=9600
    	conn.serial.bytesize=8
    	conn.serial.parity=serial.PARITY_NONE
    	conn.serial.stopbits=1
    	conn.serial.timeout=0.1
    	conn.mode=minimalmodbus.MODE_ASCII
    	conn.address=address
        #tep=conn.read_register(2,3,4,signed=False)
        #tec=calcFromA(100,0,tep)

        #if name == 'python':


    except Exception as e:
       print("error:" + str(e))

def canhot485(address):
    import RPi.GPIO as GPIO
    EN_485 =  4
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(EN_485,GPIO.OUT)
    GPIO.output(EN_485,GPIO.HIGH)
    try:
    	conn=minimalmodbus.Instrument('/dev/ttyS0',0)
    	conn.serial.baudrate=9600
    	conn.serial.bytesize=8
    	conn.serial.parity=serial.PARITY_NONE
    	conn.serial.stopbits=1
    	conn.serial.timeout=0.1
    	conn.mode=minimalmodbus.MODE_ASCII
    except Exception as e:
       print("error:" + str(e))
    finally:
    	GPIO.cleanup()
