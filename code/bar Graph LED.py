import machine
import utime

A_LED = machine.Pin(16,machine.Pin.OUT)  #Create an output pin for each segment
B_LED = machine.Pin(17,machine.Pin.OUT)  
C_LED = machine.Pin(18,machine.Pin.OUT)  
D_LED = machine.Pin(19,machine.Pin.OUT)  
E_LED = machine.Pin(20,machine.Pin.OUT)  
F_LED = machine.Pin(21,machine.Pin.OUT)  
G_LED = machine.Pin(22,machine.Pin.OUT)  
H_LED = machine.Pin(26,machine.Pin.OUT)  
I_LED = machine.Pin(27,machine.Pin.OUT)  
J_LED = machine.Pin(28,machine.Pin.OUT)  

print("Ready, Set, GO!")
Seq_Del = .1
while True:
    A_LED.value(1)       #Turn ON LED Bars in sequence
    utime.sleep(Seq_Del) #Pause a bit
    B_LED.value(1)       
    utime.sleep(Seq_Del) 
    C_LED.value(1)       
    utime.sleep(Seq_Del) 
    D_LED.value(1)       
    utime.sleep(Seq_Del) 
    E_LED.value(1)       
    utime.sleep(Seq_Del) 
    F_LED.value(1)       
    utime.sleep(Seq_Del) 
    G_LED.value(1)       
    utime.sleep(Seq_Del) 
    H_LED.value(1)       
    utime.sleep(Seq_Del) 
    I_LED.value(1)       
    utime.sleep(Seq_Del) 
    J_LED.value(1)       
    utime.sleep(Seq_Del) 

    utime.sleep(1) 
    
    A_LED.value(0)        #Turn OFF LED Bars in same sequence
    utime.sleep(Seq_Del)
    B_LED.value(0)
    utime.sleep(Seq_Del)
    C_LED.value(0)
    utime.sleep(Seq_Del)
    D_LED.value(0)
    utime.sleep(Seq_Del)
    E_LED.value(0)
    utime.sleep(Seq_Del)
    F_LED.value(0)
    utime.sleep(Seq_Del)
    G_LED.value(0)
    utime.sleep(Seq_Del)
    H_LED.value(0)
    utime.sleep(Seq_Del)
    I_LED.value(0)
    utime.sleep(Seq_Del)
    J_LED.value(0)
    utime.sleep(Seq_Del)

    utime.sleep(1) 
