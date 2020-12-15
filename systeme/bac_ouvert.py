# Imports
import time
import RPi.GPIO as GPIO
import threading

  # Definition des pins
pinBtn =38



# Definition pin en entree
GPIO.setup(pinBtn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


class thread_bac_ouvert(threading.Thread):
    
    def __init__(self,stop_event):
        threading.Thread.__init__(self)
        self.stop_event=stop_event
        
        # initialisation de la variable qui portera le résultat
        self.resultat = None
      
    def run(self):

        
        # Boucle infinie
        while not self.stop_event.wait(1):
            etat = GPIO.input(pinBtn)
            
            # etat==0 => bouton appuye => LED allumee
            if (etat == 0):
                print("interrupteur relaché (bac)")
                self.resultat = True
            if (etat==1):
                self.resultat = False
            
                
                
                        
            # Temps de repos pour eviter la surchauffe du processeur
            time.sleep(0.0005)

          
    def result(self):
        return self.resultat


