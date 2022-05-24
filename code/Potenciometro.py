
import time
import board
import analogio

potentiometer = analogio.AnalogIn(board.GP26)

get_voltage = 3.3 / 65535

while True:
    voltage = potentiometer.value * get_voltage
    print(voltage)
    time.sleep(2)