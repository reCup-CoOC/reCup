# -*- coding: utf-8 -*-

### Définition classe ###
# Casier

class Casier:
    "Définition d'un casier "
    # Constructeur
    def __init__(self):
        #colonnes
        self.p1 = 0
        self.p2 = 0
        self.g1 = 0
        self.g2 = 0

        #Drapeaux états
        self.full_petites = False
        self.full_grandes = False
        
    
    #ajoute une tasse dans une colonne
    def add_tasse_p1(self):
        self.p1 += 1 

    def add_tasse_p2(self):
        self.p2 += 1
        
    def add_tasse_g1(self):
        self.g1 += 1
        
    def add_tasse_g2(self):
        self.g2 += 1

    #lever les drapeaux
    def tofull_petites(self):
        self.full_petites = True
        
    def tofull_grandes(self):
        self.full_grandes = True

    #clear
    def clear(self):
        self.p1 = 0
        self.p2 = 0
        self.g1 = 0
        self.g2 = 0
        self.full_petites = False
        self.full_grandes = False
    

