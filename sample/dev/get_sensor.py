import os                                          
import glob                                        
import time                                        
import RPi.GPIO as GPIO
import smbus
from datetime import datetime
import MySQLdb

db = MySQLdb.connect("localhost","root","aquaponic","aquaponic" )
cursor = db.cursor()

address = 0x48
A0 = 0x40
A1 = 0x41
A2 = 0x42
A3 = 0x43
A = [0x40, 0x41]
bus = smbus.SMBus(1)
value = [0]*2

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

os.system('modprobe w1-gpio')                             
os.system('modprobe w1-therm')                                                 
base_dir = '/sys/bus/w1/devices/'                         

device_folder = [0]*4
device_file = [0]*4
f = [0]*4
lines = [0]*4
equals_pos = [0]*4
temp_string = [0]*4
temp_c = [0]*4

for i in range(0,4):
	device_folder[i] = glob.glob(base_dir + '28*')[i]          
	device_file[i] = device_folder[i] + '/w1_slave'            
	print device_folder[i]

def read_temp_raw(i):
	   f[i] = open(device_file[i], 'r')
	   lines[i] = f[i].readlines()                             
	   f[i].close()
           return lines[i]

def read_temp(i):
	   lines[i] = read_temp_raw(i)
	   while lines[i][0].strip()[-3:] != 'YES':                
	      time.sleep(0.2)
	      lines[i] = read_temp_raw(i)
	   equals_pos[i] = lines[i][1].find('t=')                  
	   if equals_pos[i] != -1:
	      temp_string[i] = lines[i][1][equals_pos[i]+2:]
	      temp_c[i] = float(temp_string[i]) / 1000.0           
	      return temp_c[i]

while True:
   try :
	for i in range(0,2):
	    bus.write_byte(address,A[i])
	    value[i] = bus.read_byte(address)
	    time.sleep(0.1)
        _id = 'A000123'
	_recv = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	_a0 = value[0]*5.0/255
	_a1 = value[1]*5.0/255
	_l1 = GPIO.input(22)
	_l2 = GPIO.input(27)
	_t0 = read_temp(0)
	_t1 = read_temp(1)
	_t2 = read_temp(2)
	_t3 = read_temp(3)
	_sel = 1
	print "AIN 1 : " + "{:.2f}".format(_a0) + " AIN 2 : " + "{:.2f}".format(_a1) +  " Limit 1 : " + str(_l1) + " Limit 2 : " + str(_l2) + "  T1 : " + str(_t0) , "  T2 : " + str(_t1) + " T3 : " + str(_t2) , "  T4 : " + str(_t3) 
	sql = """INSERT INTO sensor_data(ID,
        	RECV, A0, A1, LIMIT1, LIMIT2, T0, T1, T2, T3, VALVE)
        	VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" %(_id,_recv,_a0,_a1,_l1,_l2,_t0,_t1,_t2,_t3,_sel)
	cursor.execute(sql)
	db.commit()
   except :
        db.rollback()

db.close()

