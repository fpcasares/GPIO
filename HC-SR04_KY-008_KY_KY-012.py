#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import _thread


#GPIO Setup   
GPIO_14="cable verde"
GPIO_15="cable rojo"
GPIO_18="cable blanco"
VCC="cable amarillo"
GND="cable naranja"
V3="cable azul"

TRIGGER = 15
ECHO = 18
LASER = 14

GPIO.setmode(GPIO.BCM)

GPIO.setup(LASER, GPIO.OUT)
GPIO.setup(TRIGGER,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)


GPIO.output(TRIGGER,False)

GPIO.output(LASER,False)


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

def get_continue_distance():
    while True:
        get_distance()


def show():
    global pw
    print(pw)


def laser():
    while True:
        time.sleep(0.1)
        distance=get_distance()
        if distance < 2.000:
            distance = 0
        elif distance >30.000:
            distance = 30.000
        print(distance)
        pw=distance/100
        GPIO.output(LASER,False)
        time.sleep(pw)
        GPIO.output(LASER,True)
        time.sleep(pw)
         
 

laser()






GPIO.cleanup()

