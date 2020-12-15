# Imports
import time
import RPi.GPIO as GPIO
import threading
import machine

  # Definition des pins
pinBtn =35



# Definition pin en entree
GPIO.setup(pinBtn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)



      
def presence_plateau_distri():
        i=0
        resultat=False
        # Boucle infinie
        while not resultat:
            etat = GPIO.input(pinBtn)
            i=i+1
            # etat==0 => bouton appuye => LED allumee
            if (etat == 0):
                print("plateau non présent à l'état d'attente")
                resultat = False
                if i==3:
                    machine.init_machine()
            if (etat==1):
                resultat = True
                
                        
            # Temps de repos pour eviter la surchauffe du processeur
            time.sleep(1)

          



