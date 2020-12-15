import RPi.GPIO as GPIO
import time







def AngleToDuty(ang):
  return float(ang)/10.+5.
  



#setup sweep parameters
def position_bloque():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(36, GPIO.OUT)
    GPIO.setwarnings(False)
    
    pwm=GPIO.PWM(36,100)
    pwm.start(90)
    depart =0
    arrivee=95
    DELAY=0.1
    incStep=5
    pos=depart

   
    pwm.start(AngleToDuty(pos)) #star pwm
    nbRun=1
    
    
    for pos in range(depart,arrivee,incStep):
            duty=AngleToDuty(pos)
            pwm.ChangeDutyCycle(duty)
            time.sleep(DELAY)
    print("position: {}° -> duty cycle : {}%".format(pos,duty))
    pwm.stop() #stop sending value to output
    
        
        
      
    
    
    
def position_libre():
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(36, GPIO.OUT)
    GPIO.setwarnings(False)
    
    pwm=GPIO.PWM(36,100)
    pwm.start(90)
    depart =0
    arrivee=140
    DELAY=0.1
    incStep=5
    pos=depart

   
   
   
        
    for pos in range(depart,arrivee,incStep):
            duty=AngleToDuty(pos)
            pwm.ChangeDutyCycle(duty)
            time.sleep(DELAY)
    print("position: {}° -> duty cycle : {}%".format(pos,duty))
    pwm.stop() #stop sending value to output
    
    time.sleep(2)
    
    pwm.start(AngleToDuty(pos)) #star pwm
    for pos in range(arrivee,depart,-incStep):
            duty=AngleToDuty(pos)
            pwm.ChangeDutyCycle(duty)
            time.sleep(DELAY)
    print("position: {}° -> duty cycle : {}%".format(pos,duty))
    
    
    
    
def liberer_tasse():
    

    position_libre()
#     time.sleep(2)
#     position_bloque()
#     
    
    


    
