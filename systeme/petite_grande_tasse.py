# Imports
import time
import RPi.GPIO as GPIO
import threading

  # Definition des pins
pinBtn =33



# Definition pin en entree
GPIO.setup(pinBtn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


class thread_petite_grande_tasse(threading.Thread):
    
    def __init__(self,stop_event):
        threading.Thread.__init__(self)
        self.stop_event=stop_event
        
        # initialisation de la variable qui portera le résultat
        self.resultat = None
      
    def run(self):

        
        # Boucle infinie
        while not self.stop_event.wait(1):
            etat = GPIO.input(pinBtn)
            
            # etat==1 => bouton appuye => LED allumee
            
            if (etat==1):
                self.resultat = True
                print("grande")
            
                
                
                        
            # Temps de repos pour eviter la surchauffe du processeur
            time.sleep(0.005)

          
    def result(self):
        return self.resultat


