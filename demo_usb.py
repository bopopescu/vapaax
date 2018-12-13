# -*- coding:utf-8 -*-
#import can485
import usb485

rh=usb485.get_RH()
print (rh)

temp=usb485.get_T()
print (temp)

soil=usb485.get_T_soil()
print (soil)

usb485.set_motor(0)
