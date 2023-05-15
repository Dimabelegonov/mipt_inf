import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
for _ in range(5):
    GPIO.output(14, 1)
    print("1")
    time.sleep(1)
    GPIO.output(14, 0)
    print("2")
    time.sleep(1)
