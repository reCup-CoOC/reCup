# Imports
import time
import RPi.GPIO as GPIO
import threading

  # Definition des pins
pinBtn = 37



# Definition pin en entree
GPIO.setup(pinBtn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


class thread_bouton_terminer(threading.Thread):
    
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
            if (etat == 1):
                print("Appui detecte")
                self.resultat = True
                
                        
            # Temps de repos pour eviter la surchauffe du processeur
            time.sleep(0.005)
        self.resultat = True
          
    def result(self):
        return self.resultat