#---------------------------------------------------------------------#
#Name - IR&NECDataSend.py
#Description - Sends data from the IR sensor but uses the official NEC Protocol (command line version)
#Date - 07/04/20 - 18/08/19
#---------------------------------------------------------------------#
#Imports modules
import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime


#==================#
#Promps for values
#Input pin
while True:
	PinIn = input("Please enter your GPIO output pin: ")
	try:
		PinIn = int(PinIn)
		break
	except:
		pass



#==================#
#Sets up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PinIn,GPIO.OUT)



#==================#
#Defines Subs	
def ConvertBin(HexVal): #Converts hexidecimal data to binary data
    if HexVal[:2]=='0x':
        HexVal=HexVal[2:]	
    scale = 16 ## equals to hexadecimal
    num_of_bits = 4*len(HexVal)
    return(bin(int(HexVal, scale))[2:].zfill(num_of_bits))
