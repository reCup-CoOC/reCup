# -*- coding: utf-8 -*-

### Définition classe ###
# Tasse

class Tasse:
    "Définition d'une tasse "
    # Constructeur
    def __init__(self):
        #par défaut tasse grande, comme ça si pb de détection d'une petite tasse, se retrouve dans un emplacement grandre
        
        self.grande = True

    def to_petite(self):
        self.grande = False
        
        