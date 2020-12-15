#!/usr/bin/env python3.5
#-- coding: utf-8 --

import RPi.GPIO as GPIO #Importe la bibliothèque pour contrôler les GPIOs
from pirc522 import RFID
import time
import threading



GPIO.setmode(GPIO.BOARD) #Définit le mode de numérotation (Board)
GPIO.setwarnings(False) #On désactive les messages d'alerte

rc522 = RFID() #On instancie la lib


print('En attente d\'un badge (pour quitter, Ctrl + c): ') #On affiche un message demandant à l'utilisateur de passer son badge


class thread_rfid_lecture(threading.Thread):
    
    def __init__(self,stop_event):
        threading.Thread.__init__(self)
        self.stop_event=stop_event
        
        # initialisation de la variable qui portera le résultat
        self.id = None

    def run(self):
  
    #On va faire une boucle infinie pour lire en boucle
        while not self.stop_event.wait(1):
      
            rc522.wait_for_tag() #On attnd qu'une puce RFID passe à portée
            (error, tag_type) = rc522.request() #Quand une puce a été lue, on récupère ses infos

            if not error : #Si on a pas d'erreur
                (error, uid) = rc522.anticoll() #On nettoie les possibles collisions, ça arrive si plusieurs cartes passent en même temps

            if not error :
                #Si on a réussi à nettoyer
                self.id = format(uid)
               # print('Vous avez passé le badge avec l\'id : {}'.format(uid)) #On affiche l'identifiant unique du badge RFID
                break
            
    def result(self):
        return self.id

        
               
                
