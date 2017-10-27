#!/usr/bin/env python
# This program makes an LED light on a Raspberry Pi blink 'Hello World' in morse code.

import RPi.GPIO as GPIO
import time

# Set up GPIO board so that pin 11 is output
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

# Dictionary of morse codes for the needed letters
codes = {
    "H": ["short", "short", "short", "short"],
    "E": ["short"],
    "L": ["short", "long", "long", "short"],
    "O": ["long", "long", "long"],
    "W": ["short", "long", "long"],
    "R": ["short", "long", "short"],
    "D": ["long", "short", "short"]
}

def morse_code(str):
    # Split the string into a list of characters
    letters = list(str)
    for letter in letters:
        if letter.upper() in codes:
            # Loops through the list of longs and shorts for each letter
            for blink in codes[letter.upper()]:
                # Short blink lasts for one second
                if blink == "short":
                    GPIO.output(11, True)
                    time.sleep(1)
                    GPIO.output(11, False)
                    time.sleep(1)
                    print("short")
                # Long blink lasts for three seconds
                elif blink == "long":
                    GPIO.output(11, True)
                    time.sleep(3)
                    GPIO.output(11, False)
                    time.sleep(3)
                    print("long")

morse_code("HELLO WORLD")
