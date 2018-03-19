#!/usr/bin/python
#show "Hello World on the lcd screen"
#

import Adafruit_CharLCD as LCD
import time
import subprocess

lcd = LCD.Adafruit_CharLCDPlate()
Name = subprocess.check_output(['hostname']).strip()
IPaddr = subprocess.check_output(['hostname','-I']).split()

displayText = "Hello World"
displayText1 = Name + '\n' + IPaddr[0]
refresh = True


while (True):
    if lcd.is_pressed(LCD.SELECT):
        lcd.clear()
        lcd.message(Name + '\n' + displayText)
        refresh = True
    else:
        if refresh:
            lcd.clear()
            lcd.message(displayText1)
            refresh = False
    time.sleep(0.5)