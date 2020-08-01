import RPi.GPIO as GPIO
import time

#GPIO Setup   
GPIO_14="cable verde"
GPIO_15="cable rojo"
GPIO_18="cable blanco"
VCC="cable amarillo"
GND="cable naranja"
V3="cable azul"

TRIGGER = 15
ECHO = 18
GPIO_PIN_OUT = 14

GPIO.setmode(GPIO.BCM)

GPIO.setup(GPIO_PIN_OUT, GPIO.OUT)
GPIO.setup(TRIGGER,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)


GPIO.output(TRIGGER,False)




def get_distance():
    GPIO.output(TRIGGER,True)
    time.sleep(0.00001)
    GPIO.output(TRIGGER,False)

    while GPIO.input(ECHO)==0:
      pulse_start = time.time()
    while GPIO.input(ECHO)==1:
      pulse_end = time.time()   

    pulse_duration =pulse_end - pulse_start  
    distance= pulse_duration * 17150
    distance = round(distance,3)
    return(distance)


while True:
    print(get_distance())
    





GPIO.cleanup()
