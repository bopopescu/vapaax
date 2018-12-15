# -*- coding:utf-8 -*-
import vapaa
import time

#實作1 :起手式
vapaa = vapaa.conn('COM6') #請依com編號修改
print (vapaa.ai(1,'RH')) #ai(端口, 連接感測器類型：T:溫度 | RH:溼度 | soil:土壤)
vapaa.do(1,0) #do(端口, 0:開 | 1:關)
