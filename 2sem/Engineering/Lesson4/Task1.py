import RPi.GPIO as GPIO


def get_a():
    a = input("Enter a number between 0 and 255:")
    return a


def dec2bin(a):
    b = str(bin(a)[2:])
    while len(b) != 8:
        b = "0" + b
    return b


GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

try:
    a = get_a()
    while (a != "q"):

        if a.isdigit():
            a = float(a)
            if a != int(a):
                print("Error")
                a = get_a()
                continue
            elif a < 0 or a > 255:
                print("Error")
                a = get_a()
                continue
        else:
            print("Error")
            a = get_a()
            continue

        a = int(a)
        b = dec2bin()
        t = 3.3 / 255

        print("Voltage:", t * a)
        number = [int(b[i]) for i in range(8)]

        GPIO.output(dac, number)
        a = get_a()

except KeyboardInterrupt:
    print("\nProgram has ended")
finally:
    GPIO.output(dac, [0, 0, 0, 0, 0, 0, 0, 0])
    GPIO.cleanup()
