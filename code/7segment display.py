import tm1637
from machine import pin
from utime import sleep

dispaly = tm1637 . TM1637(clk=pin(16), dio=pin(17))
dispaly.show(“pico”)
sleep(1)



dispaly.number(-123)
sleep(1)

dispaly.numbers(12,59)
sleep(1)

#adjust the brightness to make it lower
dispaly.brightness(0)
sleep(1)



dispaly.temperature(99)
sleep(1)
