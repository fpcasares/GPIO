import RPi.GPIO as GPIO

 #GPIO Setup   
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.output(14, True)


while not KeyboardInterrupt:
    GPIO.output(14, True)
    time.sleep(1)
    GPIO.output(14, False)
    time.sleep(1)

GPIO.cleanup()

GPIO_14="cable verde"
GPIO_15="cable rojo"
VCC="cable amarillo"
GND="cable naranja"
