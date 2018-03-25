import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)
while True :

	GPIO.output(26, GPIO.HIGH)
	print "HIGH"
	time.sleep(4)
        GPIO.output(26, GPIO.LOW)
	print "LOW"
        time.sleep(4)
