from Motor import *
from servo import *
from Ultrasonic import *
from Led import *
import time

motor = Motor()
servo = Servo()
ultrasonic = Ultrasonic()
led=Led()

def check_distance():
    #distance = integer
    distance = ultrasonic.get_distance()
    return distance

def speed_control():
    try:
        servo.setServoPwm('0',90) #make the sensor face the front of the car
        speed =0  #initial speed is zero
        while True:
            sonic_distance1 = check_distance()     #check the initial distance
            sonic_distance2 = check_distance()     #check the final distance
            print(sonic_distance1)    #print the initial distance
            print(sonic_distance2)    #print the initial distance
            distance_change= sonic_distance2 - sonic_distance1  #distance change from the initial distance and the final distance
            
            if distance_change > 30 and sonic_distance2 >30:  #speeding up fast
                if speed<900:
                    speed = speed + 100
                    motor.setMotorModel(speed,speed,speed,speed)
                    print(f"Your distance is {sonic_distance2}")
                    print(f"Speeding Up Fast, Your speed is {speed}")
                    led.ledIndex(0x01,0,255,255)  #show the led cyan-blue
                    led.ledIndex(0x02,0,255,255)
                    led.ledIndex(0x04,0,255,255)
                    led.ledIndex(0x08,0,255,255)
                    led.ledIndex(0x10,0,255,255)
                    led.ledIndex(0x20,0,255,255)
                    led.ledIndex(0x40,0,255,255)
                    led.ledIndex(0x80,0,255,255)

                    
                    time.sleep(.5)
                else:
                    speed = 1000
                    motor.setMotorModel(speed,speed,speed,speed)
                    print(f"Your distance is {sonic_distance2}")
                    print(f"Speeding Up Fast, Your speed is {speed}")
                    led.ledIndex(0x01,0,255,255)  #show the led cyan-blue
                    led.ledIndex(0x02,0,255,255)
                    led.ledIndex(0x04,0,255,255)
                    led.ledIndex(0x08,0,255,255)
                    led.ledIndex(0x10,0,255,255)
                    led.ledIndex(0x20,0,255,255)
                    led.ledIndex(0x40,0,255,255)
                    led.ledIndex(0x80,0,255,255)
                    time.sleep(.5)
                
            elif distance_change > 10 and sonic_distance2 >30:  #speeding up slowly
                if speed<900:
                    speed = speed + 30
                    motor.setMotorModel(speed,speed,speed,speed)
                    print(f"Your distance is {sonic_distance2}")
                    print(f"Speeding Up slow, Your speed is {speed}")
                    led.ledIndex(0x01,0,0,255)  #show the led blue
                    led.ledIndex(0x02,0,0,255)
                    led.ledIndex(0x04,0,0,255)
                    led.ledIndex(0x08,0,0,255)
                    led.ledIndex(0x10,0,0,255)
                    led.ledIndex(0x20,0,0,255)
                    led.ledIndex(0x40,0,0,255)
                    led.ledIndex(0x80,0,0,255)
                    
                    time.sleep(.5)
                else:
                    speed = 930
                    motor.setMotorModel(speed,speed,speed,speed)
                    print(f"Your distance is {sonic_distance2}")
                    print(f"Speeding Up slow, Your speed is {speed}")
                    led.ledIndex(0x01,0,0,255)  #show the led blue
                    led.ledIndex(0x02,0,0,255)
                    led.ledIndex(0x04,0,0,255)
                    led.ledIndex(0x08,0,0,255)
                    led.ledIndex(0x10,0,0,255)
                    led.ledIndex(0x20,0,0,255)
                    led.ledIndex(0x40,0,0,255)
                    led.ledIndex(0x80,0,0,255)
                    time.sleep(.5)
            
            elif distance_change > -10 and distance_change < 10 and sonic_distance2 > 30:  #speed maintaining
                if speed <1000:
                    speed =700
                    motor.setMotorModel(speed,speed,speed,speed)
                    print(f"Your distance is {sonic_distance2}")
                    print(f"Speed Maintaining, Your speed is {speed}")
                    led.ledIndex(0x01,0,255,0)  #show the led green
                    led.ledIndex(0x02,0,255,0)
                    led.ledIndex(0x04,0,255,0)
                    led.ledIndex(0x08,0,255,0)
                    led.ledIndex(0x10,0,255,0)
                    led.ledIndex(0x20,0,255,0)
                    led.ledIndex(0x40,0,255,0)
                    led.ledIndex(0x80,0,255,0)
                    time.sleep(.5)
                else:
                    speed = 700
                    motor.setMotorModel(speed,speed,speed,speed)
                    print(f"Your distance is {sonic_distance2}")
                    print(f"Speed Maintaining, Your speed is {speed}")
                    led.ledIndex(0x01,0,255,0)  #show the led green
                    led.ledIndex(0x02,0,255,0)
                    led.ledIndex(0x04,0,255,0)
                    led.ledIndex(0x08,0,255,0)
                    led.ledIndex(0x10,0,255,0)
                    led.ledIndex(0x20,0,255,0)
                    led.ledIndex(0x40,0,255,0)
                    led.ledIndex(0x80,0,255,0)
                    
                    time.sleep(.5)
            
            elif distance_change < -10 and distance_change >-30 and sonic_distance2 > 30:  #speed decreasing slow
                if speed > 530:
                    speed = speed -30
                    motor.setMotorModel(speed,speed,speed,speed)
                    print(f"Your distance is {sonic_distance2}")
                    print(f"Speeding Down slow, Your speed is {speed}")
                    led.ledIndex(0x01,255,255,0) #show the led yellow
                    led.ledIndex(0x02,255,255,0)
                    led.ledIndex(0x04,255,255,0)
                    led.ledIndex(0x08,255,255,0)
                    led.ledIndex(0x10,255,255,0)
                    led.ledIndex(0x20,255,255,0)
                    led.ledIndex(0x40,255,255,0)
                    led.ledIndex(0x80,255,255,0)
                    time.sleep(.5)
                else:
                    speed = 500
                    motor.setMotorModel(speed,speed,speed,speed)
                    print(f"Your distance is {sonic_distance2}")
                    print(f"Speeding Down slow, Your speed is {speed}")
                    led.ledIndex(0x01,255,255,0)  #show the led yellow
                    led.ledIndex(0x02,255,255,0)
                    led.ledIndex(0x04,255,255,0)
                    led.ledIndex(0x08,255,255,0)
                    led.ledIndex(0x10,255,255,0)
                    led.ledIndex(0x20,255,255,0)
                    led.ledIndex(0x40,255,255,0)
                    led.ledIndex(0x80,255,255,0)
                    
                    
                    time.sleep(.5)
                
            elif distance_change < -30 and sonic_distance2 > 30:  #speed decreasing fast
                if speed > 600:
                    speed = speed -100
                    motor.setMotorModel(speed,speed,speed,speed)
                    print(f"Your distance is {sonic_distance2}")
                    print(f"Speeding Down fast, Your speed is {speed}")
                    led.ledIndex(0x01,255,125,0) #show the led orange
                    led.ledIndex(0x02,255,125,0)
                    led.ledIndex(0x04,255,125,0)
                    led.ledIndex(0x08,255,125,0)
                    led.ledIndex(0x10,255,125,0)
                    led.ledIndex(0x20,255,125,0)
                    led.ledIndex(0x40,255,125,0)
                    led.ledIndex(0x80,255,125,0)
                    
                    time.sleep(.5)
                else:
                    speed = 500
                    motor.setMotorModel(speed,speed,speed,speed)
                    print(f"Your distance is {sonic_distance2}")
                    print(f"Speeding Down fast, Your speed is {speed}")
                    led.ledIndex(0x01,255,125,0)  #show the led orange
                    led.ledIndex(0x02,255,125,0)
                    led.ledIndex(0x04,255,125,0)
                    led.ledIndex(0x08,255,125,0)
                    led.ledIndex(0x10,255,125,0)
                    led.ledIndex(0x20,255,125,0)
                    led.ledIndex(0x40,255,125,0)
                    led.ledIndex(0x80,255,125,0)
                    time.sleep(.5)
                
            elif sonic_distance2 < 30:  #speed zero
                speed =0
                motor.setMotorModel(speed,speed,speed,speed)
                print(f"Your distance is {sonic_distance2}")
                print(f"Stoped the car preventing the CRASH!!, your speed is {speed}")
                led.ledIndex(0x01,255,0,0)  #show the led red     
                led.ledIndex(0x02,255,0,0)   
                led.ledIndex(0x04,255,0,0) 
                led.ledIndex(0x08,255,0,0)     
                led.ledIndex(0x10,255,0,0)    
                led.ledIndex(0x20,255,0,0)     
                led.ledIndex(0x40,255,0,0)    
                led.ledIndex(0x80,255,0,0) 
                time.sleep(.5)
                
                
                
        
    except KeyboardInterrupt:
        motor.setMotorModel(0,0,0,0)
        led.colorWipe(led.strip, Color(0,0,0))

speed_control()
