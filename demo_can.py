# -*- coding:utf-8 -*-
import can485

rh=can485.get_RH()
print (rh)

temp=can485.get_T()
print (temp)

soil=can485.get_T_soil()
print (soil)

can485.set_motor(0)
