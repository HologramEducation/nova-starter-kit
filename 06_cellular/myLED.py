import RPi.GPIO as GPIO ## Import GPIO library
from time import sleep ## Allows us to use 'sleep'

## Define a function that will turn an LED on
def lightOn(LED_PIN):
    GPIO.setup(LED_PIN, GPIO.OUT) ## Setup GPIO Pin to OUT
    GPIO.output(LED_PIN,True) ## Switch on LED

## Define a function that will turn an LED off
def lightOff(LED_PIN):
    GPIO.setup(LED_PIN, GPIO.OUT) ## Setup GPIO Pin to OUT
    GPIO.output(LED_PIN,False) ## Switch on LED

## Define a function that will blink an LED once
def blink(LED_PIN):
    lightOn(LED_PIN)
    sleep(0.5)
    lightOff(LED_PIN)
    sleep(0.5)

##Define a function that asks how many times it should blink
def blinkTimes(LED_PIN):
    ## Ask user for total number of blinks
    iterations = raw_input("Enter total number of times to blink: ")

    for i in range(0,int(iterations)): ## Run loop numTimes
        print "Iteration " + str(i+1) ## Print current loop
        lightOn(LED_PIN)
        sleep(0.5)
        lightOff(LED_PIN)
        sleep(0.5)

    print "Done" ## When loop is complete, print "Done"
