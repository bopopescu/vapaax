# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import serial
import minimalmodbus


EN_485 =  4
GPIO.setmode(GPIO.BCM)
GPIO.setup(EN_485,GPIO.OUT)
GPIO.output(EN_485,GPIO.HIGH)


#
def calcFromA(max,min,data):
    return ((max-min)/16)*(data-4)+min
#電壓
def calcFromV(max,min,data):
    return ((max-min)/10)*data+min



try:
	conn=minimalmodbus.Instrument('/dev/ttyS0',0)
	conn.serial.baudrate=9600
	conn.serial.bytesize=8
	conn.serial.parity=serial.PARITY_NONE
	conn.serial.stopbits=1
	conn.serial.timeout=0.1
	conn.mode=minimalmodbus.MODE_ASCII

	conn.address=97
	tep=conn.read_register(2,3,4,signed=False)
	tec=calcFromA(100,0,tep)


	#conn.address=33
	#conn.write_bit(1,0,15)


except Exception as e:
   print("error:" + str(e))
finally:
	GPIO.cleanup()
