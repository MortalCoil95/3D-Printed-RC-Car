
from machine import Pin, PWM
from dcmotor import DCMotor       
   
from time import sleep     
frequency = 15000       
pin1 = Pin(5, Pin.OUT)    
pin2 = Pin(4, Pin.OUT)
p2 = machine.Pin(2)
pwm2 = machine.PWM(p2)
enable = PWM(Pin(13), frequency)  
dc_motor = DCMotor(pin1, pin2, enable)      
dc_motor = DCMotor(pin1, pin2, enable, 350, 1023)
dc_motor.forward(50)    
sleep(10)        
dc_motor.stop()  
sleep(10)    
dc_motor.backwards(100)  
sleep(10)       
dc_motor.forward(60)
sleep(10)
dc_motor.stop()

pwm2.freq(50)
 
while True:
    for d in range(18,22,1):
        # set the duty cycle to d .i.e. 18 through 115 with step of 1
        pwm2.duty(d)
        tSleep = (d/1023)*20
        time.sleep(tSleep)
        # print the pwm details like pin, freq, duty cycle
        print (pwm2)
    time.sleep(2)