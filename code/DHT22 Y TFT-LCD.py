
from ILI9488_V01 import ILI9488
from machine import Pin, SPI
from micropython import const
import Roboto24_Med, RobotoBlack32_180
import time,utime,framebuf
from DHT22 import DHT22
from Temperature_icon import *
SCREEN_WIDTH = const(480)
SCREEN_HEIGHT = const(320)
SCREEN_ROT = const(1)
TFT_CLK_PIN = const(6)
TFT_MOSI_PIN = const(7)
TFT_MISO_PIN = const(4)
TFT_CS_PIN = const(0)
TFT_RST_PIN = const(1)
TFT_DC_PIN = const(2)
COLOR_WHITE = const(0xFFFF)
COLOR_BLACK = const(0x0000)
COLOR_DARK_GRAY = const(0xC618)
COLOR_LIGHT_GRAY = const(0xEF7D)
COLOR_RED = const(0xF100)
COLOR_ORANGE = const(0xFCC0)
COLOR_YELLOW = const(0xFF47) #FEB3B
COLOR_GREEN = const(0x0770)
COLOR_BLUE = const(0x001F)
PRIMARY_DARK_C = const(0x0017)
PRIMARY_NORMAL_C = const (0x601D)
PRIMARY_LITE_C = const(0x9A5F)
SECONDARY_DARK_C = const(0x8C71)
SECONDARY_LITE_C = const(0xEF7D)
SECONDARY_NORMAL_C = const(0xBDD7)
#Initialize the onboard LED as output
led = machine.Pin(25,machine.Pin.OUT)
#Initialize SPI
spi = SPI(0,baudrate=40000000,miso=Pin(TFT_MISO_PIN),mosi=Pin(TFT_MOSI_PIN),sck=Pin(TFT_CLK_PIN))
# DHT22 libray is available at
# https://github.com/danjperron/PicoDHT22
# Initialize DHT22
dht22 = DHT22(Pin(13,Pin.IN,Pin.PULL_UP))
#Initialize TFT Display
display = ILI9488(spi,cs=Pin(TFT_CS_PIN),dc=Pin(TFT_DC_PIN),rst=Pin(TFT_RST_PIN),
                  w=SCREEN_WIDTH, h=SCREEN_HEIGHT,r=SCREEN_ROT)
display.FillRectangle(0,0,SCREEN_WIDTH,SCREEN_HEIGHT,PRIMARY_DARK_C) #Clear Screen
# Toggle LED funtionality
def BlinkLED(timer_one):
    led.toggle()
 
# Read the sensor and calculate / screen the temperature -- humidity values
def ReadDHT22Sensor(timer_two):
    T, H = dht22.read() # Read Sensor
    if T is None:
        print(" sensor error")
    else:
        F = ( T * 1.8 ) + 32 # Fahrenheit # T(°F) = T(°C) × 9/5 + 32
        K = T + 273.15 # Kelvin # T(K) = T(°C) + 273.15          
        R = (T + 273.15) * 1.8 # Rankine # T(°R) = (T(°C) + 273.15) × 9/5          
        display.SetFont(RobotoBlack32_180)
        display.SetFgBgColor(COLOR_BLACK, SECONDARY_NORMAL_C)
        display.FillRectangle(cx+30,cy+40,cw-32,35,SECONDARY_NORMAL_C)
        display.WriteString(cx+30,cy+40,"{:0.2f}".format(T)+ "°C")
        
        display.FillRectangle(fx+30,fy+40,fw-32,35,SECONDARY_NORMAL_C)
        display.WriteString(fx+30,fy+40,"{:0.2f}".format(F)+ "°F")
        
        display.FillRectangle(kx+10,ky+40,kw-12,35,SECONDARY_NORMAL_C)
        display.WriteString(kx+10,ky+40,"{:0.2f}".format(K)+ "°K")
        
        display.FillRectangle(rx+10,ry+40,rw-12,35,SECONDARY_NORMAL_C)
        display.WriteString(rx+10,ry+40,"{:0.2f}".format(R)+ "°R")
        
        display.FillRectangle(hx+110,hy+40,hw-112,35,SECONDARY_NORMAL_C)
        display.WriteString(hx+110,hy+40,"{:0.2f}".format(H)+ " %")
       
x1 = 5; y1 = 5; w1 = 470; h1 = 50
display.FillRectangle(x1,y1,w1,h1,SECONDARY_DARK_C) 
# Draw header and set Roboto32 font for headings
display.SetFgBgColor(COLOR_WHITE, PRIMARY_DARK_C)
display.SetFont(RobotoBlack32_180)
x11 = 0; y11 = 0; w11 = 480; h11 = 50
display.FillRectangle(x11,y11,w11,h11,PRIMARY_DARK_C)
display.FillRectangle(x11,y11+h11,w11,320-h11,SECONDARY_DARK_C)
display.FillRectangle(x11,y11+315,w11,5,PRIMARY_DARK_C)
display.WriteString(x11+150,y11+10,"DH22 SENSOR")
# Draw icon window
x12 = 4; y12 = 55; w12 = 150
h12 = 320 - y12 - 10
display.FillRectangle(x12,y12,w12,h12,PRIMARY_NORMAL_C)
# Draw Celsius window and set Roboto24 font for headings
cx = x12 + w12 + 3; cy = 55; cw = 158; ch = 82
display.FillRectangle(cx,cy,cw,ch-2,SECONDARY_NORMAL_C)
display.FillRectangle(cx,cy,cw,30,PRIMARY_NORMAL_C)
display.SetFgBgColor(COLOR_WHITE, PRIMARY_NORMAL_C)
display.SetFont(Roboto24_Med)
display.WriteString(cx+30,cy+3,"CELSIUS")
# Draw Fahernheit window
fx = cx+cw+3; fy = 55; fw = 158; fh = 82
display.FillRectangle(fx,fy,fw,fh-2,SECONDARY_NORMAL_C)
display.FillRectangle(fx,fy,fw,30,PRIMARY_NORMAL_C)
display.WriteString(fx+10,fy+3,"FAHRENHEIT")
# Draw Kelvin window
kx = x12 + w12 + 3; ky = cy + ch + 2; kw = 158; kh = 80
display.FillRectangle(kx,ky,kw,kh-2,SECONDARY_NORMAL_C)
display.FillRectangle(kx,ky,kw,30,PRIMARY_NORMAL_C)
display.WriteString(kx+30,ky+3,"KELVIN")
# Draw Rankine window
rx = kx + kw + 3; ry = ky; rw = 158; rh = 80
display.FillRectangle(rx,ry,rw,rh-2,SECONDARY_NORMAL_C)
display.FillRectangle(rx,ry,rw,30,PRIMARY_NORMAL_C)
display.WriteString(rx+30,ry+3,"RANKINE")
# Draw Humidity window
hx = kx; hy = ky + kh + 2; hw = 320; hh = 90
display.FillRectangle(hx,hy,hw,hh,SECONDARY_NORMAL_C)
display.FillRectangle(hx,hy,hw,30,PRIMARY_NORMAL_C)
display.WriteString(hx+110,hy+3,"HUMIDITY")
# Draw temperature / Humidity icon
k = bytearray(temperature)
fb = framebuf.FrameBuffer(k, 128, 128, framebuf.MONO_HLSB)
display.DrawBlit(fb,x12+10,y12+65,128,128)
#Initialize timer_one. Used for toggling the on board LED
timer_one = machine.Timer()
#Timer one initialization for on board blinking LED at 500mS interval
timer_one.init(freq=2, mode=machine.Timer.PERIODIC, callback=BlinkLED)
# Initialize timer_two. Used for reading DHT22.
timer_two = machine.Timer()
# Timer two initialization for reading sensor at 5 Seconds interval
timer_two.init(freq=0.2, mode=machine.Timer.PERIODIC, callback=ReadDHT22Sensor)
ReadDHT22Sensor(timer_two)