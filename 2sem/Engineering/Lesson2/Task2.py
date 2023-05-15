import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
a = int(input())
b = str(bin(a)[2:])
while len(b) != 8:
    b = "0" + b

number = [int(b[i]) for i in range(8)]

GPIO.setup(dac, GPIO.OUT)
GPIO.output(dac, number)

time.sleep(10)

GPIO.output(dac, [0, 0, 0, 0, 0, 0, 0, 0])
GPIO.cleanup()
