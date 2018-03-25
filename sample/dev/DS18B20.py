import os                                                  # import os module
import glob                                                # import glob module
import time                                                # import time module

os.system('modprobe w1-gpio')                              # load one wire communication device kernel modules
os.system('modprobe w1-therm')                                                 
base_dir = '/sys/bus/w1/devices/'                          # point to the address

device_folder = [0]*4
device_file = [0]*4
f = [0]*4
lines = [0]*4
equals_pos = [0]*4
temp_string = [0]*4
temp_c = [0]*4

for i in range(0,4):
	device_folder[i] = glob.glob(base_dir + '28*')[i]             # find device with address starting from 28*
	device_file[i] = device_folder[i] + '/w1_slave'                  # store the details
	print device_folder[i]

def read_temp_raw(i):
	   f[i] = open(device_file[i], 'r')
	   lines[i] = f[i].readlines()                                   # read the device details
	   f[i].close()
           return lines[i]

def read_temp(i):
	   lines[i] = read_temp_raw(i)
	   while lines[i][0].strip()[-3:] != 'YES':                   # ignore first line
	      time.sleep(0.2)
	      lines[i] = read_temp_raw(i)
	   equals_pos[i] = lines[i][1].find('t=')                        # find temperature in the details
	   if equals_pos[i] != -1:
	      temp_string[i] = lines[i][1][equals_pos[i]+2:]
	      temp_c[i] = float(temp_string[i]) / 1000.0                 # convert to Celcius
	      return temp_c[i]

while True:
	#for i in range(0,4):
	#   print "temp " + str(i) + " : " + str(read_temp(i))                                      # Print temperature    
	#   time.sleep(1)
	print "  T1 : " + str(read_temp(0)) , "  T2 : " + str(read_temp(1)) , "  T3 : " + str(read_temp(2)) , "  T4 : " + str(read_temp(3))
	time.sleep(1)
