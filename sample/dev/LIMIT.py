import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print GPIO.input(22), GPIO.input(27)

while True :
	print GPIO.input(22), GPIO.input(27)
	time.sleep(1)
