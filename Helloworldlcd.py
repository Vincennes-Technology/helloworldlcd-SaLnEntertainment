#!/usr/bin/python
#show "Hello World on the lcd screen"
#

import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()

displayText = "Hiya World ^-^"

lcd.clear()
lcd.message(displayText)
