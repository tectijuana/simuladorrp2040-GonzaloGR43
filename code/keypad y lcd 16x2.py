
from machine import Pin, Timer
# Import time
import time
import utime
import machine
# Import lcd_4bit_mode
import lcd_4bit_mode
# Initialize LCD pins
RS = machine.Pin(4,machine.Pin.OUT)
ENABLE = machine.Pin(5,machine.Pin.OUT)
BACK_LIGHT = machine.Pin(6,machine.Pin.OUT)
D4 = machine.Pin(0,machine.Pin.OUT)
D5 = machine.Pin(1,machine.Pin.OUT)
D6 = machine.Pin(2,machine.Pin.OUT)
D7 = machine.Pin(3,machine.Pin.OUT)                  
 
# CONSTANTS
KEY_UP   = const(0)
KEY_DOWN = const(1)
keys = [['1', '2', '3', 'A'], ['4', '5', '6', 'B'], ['7', '8', '9', 'C'], ['*', '0', '#', 'D']]
# RPi Pico pin assignments
rows = [8,9,10,11]
cols = [12,13,15,16]
# Set pins for rows as outputs
row_pins = [Pin(pin_name, mode=Pin.OUT) for pin_name in rows]
# Set pins for columns as inputs
col_pins = [Pin(pin_name, mode=Pin.IN, pull=Pin.PULL_DOWN) for pin_name in cols]
#Initialize the onboard LED as output
led = Pin(25, Pin.OUT)
#Initialize timer_one. Used for toggling the LED
timer_one = Timer()
#Initialize timer_two. Used for polling keypad
timer_two = Timer()
def BlinkLED(timer):
    led.toggle()
def InitKeypad():
    for row in range(0,4):
        for col in range(0,4):
            row_pins[row].low()
def PollKeypad(timer):
    key = None
    for row in range(4):
        for col in range(4):
            # Set the current row to high
            row_pins[row].high()
            # Check for key pressed events
            if col_pins[col].value() == KEY_DOWN:
                key = KEY_DOWN
            if col_pins[col].value() == KEY_UP:
                key = KEY_UP
            row_pins[row].low()
            if key == KEY_DOWN:
                display.WriteLine("                ",2)
                display.WriteLine("Key Pressed = "+ keys[row][col],2)
                last_key_press = keys[row][col]
# Initialize and set all the rows to low
InitKeypad()
display = lcd_4bit_mode.LCD16x2(RS,ENABLE,BACK_LIGHT,D4,D5,D6,D7)
# Turn on Back light
display.BackLightOn()
# Welcome string
display.WriteLine('    RPi PICO',1)
display.WriteLine('4x4 MatrixKeypad',2)
# Wait for five seconds
time.sleep(5)
timer_one.init(freq=5, mode=Timer.PERIODIC, callback=BlinkLED)
timer_two.init(freq=2, mode=Timer.PERIODIC, callback=PollKeypad)