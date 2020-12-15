import RPi.GPIO as GPIO
import time
from threading import Thread, RLock



Trig = 15
Echo = 16

GPIO.setup(Trig,GPIO.OUT)
GPIO.setup(Echo,GPIO.IN)

GPIO.output(Trig, False)


    
	
class thread_presence_tasse(Thread):
	def __init__(self,stop_event):
		Thread.__init__(self)
		self.distance = None
		self.presence = None
		self.stop_event=stop_event

	def run(self):
           while not self.stop_event.wait(1):
               
               GPIO.output(Trig, True)
               time.sleep(0.00001)
               GPIO.output(Trig, False)

               while GPIO.input(Echo)==0:  ## Emission de l'ultrason
                 debutImpulsion = time.time()

               while GPIO.input(Echo)==1:   ## Retour de l'Echo
                 finImpulsion = time.time()


               self.distance = round((finImpulsion - debutImpulsion) * 340 * 100 / 2, 1)  ## Vitesse du son = 340 m/s

               if (self.distance <= 5):
                   self.presence = True
                   print("objet detecté")
               elif (self.distance >= 5):
                   self.presence = False
                   time.sleep(0.5)
               time.sleep(1)       # On la prend toute les 1 seconde
	
	def result(self):
            #return self.distance
            return self.presence



