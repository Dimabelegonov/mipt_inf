import RPi.GPIO as GPIO
import time


def dec2bin(a):
    b = str(bin(a)[2:])
    while len(b) != 8:
        b = "0" + b
    return b


GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

T = float(input("Input the period:"))
try:
    while (True):

        for i in range(256):
            b = dec2bin(i)
            number = [int(b[j]) for j in range(8)]
            GPIO.output(dac, number)
            time.sleep(T / 512)

        for i in range(255, -1, -1):
            b = dec2bin(i)
            number = [int(b[j]) for j in range(8)]
            GPIO.output(dac, number)
            time.sleep(T / 512)
except KeyboardInterrupt:
    print("\nProgram has ended")
finally:
    GPIO.output(dac, [0, 0, 0, 0, 0, 0, 0, 0])
    GPIO.cleanup()
