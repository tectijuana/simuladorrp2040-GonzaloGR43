import time
import board
import digitalio

led = digitalio.DigitalInOut(board.GP14)
led.direction = digitalio.Direction.OUTPUT

while True:
  led.value = True
  time.sleep(0.5)
  led.value = False