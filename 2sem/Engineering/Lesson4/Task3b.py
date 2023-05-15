import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
p = GPIO.pwm(22, 1000)

try:
    while (True):
        duty_cycle = int(input("Input a number between 0 and 100:"))
        if duty_cycle > 100 or duty_cycle < 0:
            print("Wrong number")
            continue
        else:
            p.start(duty_cycle)
            print("Voltage:", 3.3 * duty_cycle / 100)

except KeyboardInterrupt:
    print("\nProgram has ended")
finally:
    GPIO.output(22, 0)
    GPIO.cleanup()
