# -*- coding: utf-8 -*-
from machine import *
import threading

def depose(casier,colonne):

    
    #check si stockage prêt TODO
    #vérifier que le contacteur du chariot est activé, sinon lancer init de la machine
    
    
    #traduction casier en position Z
    def Z_axis(argument):
        switcher = {
            "c1": "0",
            "c2": "100",
            "c3": "170",
        }
        return switcher.get(argument, "Invalid argument")
    z = (Z_axis(casier))
    print(z)
         
    #traduction colonne en position X
    def X_axis(argument):
        switcher = {
            "p1": "60",
            "p2": "-24",
            "g1": "-115",
            "g2": "-220",
        }
        return switcher.get(argument, "Invalid argument")
    
    x = (X_axis(colonne))
    print(x)
    
    #Dépose de la tasse
     # attendre retour true de cette fonction 
    thread = threading.Thread(target=carry_tasse(x,z))
    thread.start()

    # wait here for the result to be available before continuing
    thread.join()

    
    # return True

# init_machine()
#depose("c1","g2")