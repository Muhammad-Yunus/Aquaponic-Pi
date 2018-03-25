#!/usr/bin/python
# -*- coding:utf-8 -*-
import smbus
import time

address = 0x48
A0 = 0x40
A1 = 0x41
A2 = 0x42
A3 = 0x43
A = [0x40, 0x41]
bus = smbus.SMBus(1)
value = [0]*2
while True:
	for i in range(0,2):
	    bus.write_byte(address,A[i])
	    value[i] = bus.read_byte(address)
	    time.sleep(0.1)
	    #print "AIN " + str(i) + " : " + str(value[i]*5.0/255)
	print "AIN 1 : " + "{:.2f}".format(value[0]*5.0/255), "   AIN 2 : " + "{:.2f}".format(value[1]*5.0/255)
	time.sleep(0.1)
