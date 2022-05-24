from machine import Pin, PWM
import utime
def main():
    #Configura el Servo de 180
    servo_180 = PWM(Pin(15))
    servo_180.freq(50)
    
    #Configura el Servo de 360
    servo_360 = PWM(Pin(14))
    servo_360.freq(50)
    
    while True:
        angulo = float(input('Ingrese un ángulo: '))
        if angulo >= 0 and angulo <= 180:
            #nanosegundos
            duty = ((12.346*angulo**2 + 7777.8*angulo + 700000))
            #milisegundos
            duty /= 1000000
            #bits
            duty = int(duty*1023/20)
            
            servo_180.duty(duty) 
            servo_360.duty(duty)
        else:
            print('Digite un ángulo entre 0 y 180')
    
    
if __name__ == '__main__':
    main()