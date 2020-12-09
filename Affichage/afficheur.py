
# Importation librairie
import lcddriver
from time import sleep
import rfid


# Chargement du driver lcddriver
display = lcddriver.lcd()







def bonjour(stop_event, arg):
 sleep(0.01)# certaine fois ça place a cause d'une erreur sur les pins 
 display.lcd_clear();
 
 while not stop_event.wait(1):
  
  display.lcd_display_string("Bonjour !" , 1)
  sleep(3)
  display.lcd_clear();
  if not stop_event.wait(1):

      display.lcd_display_string("Presentez" , 1) # Affichage texte sur la 1ere ligne
      display.lcd_display_string("votre badge", 2) # Affichage texte sur la 2eme ligne
      sleep(2)
      display.lcd_clear();

  
def deposeTasse():
 sleep(0.01)# certaine fois ça place a cause d'une erreur sur les pins
 display.lcd_clear();
 display.lcd_display_string("Deposez votre " , 1) # Affichage texte sur la 1ere ligne
 display.lcd_display_string("tasse ", 2) # Affichage texte sur la 2eme ligne

def fermeTrappe():
 sleep(0.01)# certaine fois ça place a cause d'une erreur sur les pins
 display.lcd_clear();
 display.lcd_display_string("Fermez la trappe" , 1) # Affichage texte sur la 1ere ligne
 display.lcd_display_string( "S'il vous plait", 2) # Affichage texte sur la 2eme ligne
 
def bacOuvert():
  sleep(0.01)# certaine fois ça place a cause d'une erreur sur les pins 
  display.lcd_clear();
  display.lcd_display_string("  ! Attention !  " , 1) # Affichage texte sur la 1ere ligne
  display.lcd_display_string( " ! Bac Ouvert !", 2) # Affichage texte sur la 2eme ligne
 
def plateauAbsent():
  sleep(0.01)# certaine fois ça place a cause d'une erreur sur les pins  
  display.lcd_clear();
  display.lcd_display_string("un ou plusieurs  " , 1) # Affichage texte sur la 1ere ligne
  display.lcd_display_string( "plateaux absents !", 2) # Affichage texte sur la 2eme ligne
 

def plein():
 sleep(0.01)# certaine fois ça place a cause d'une erreur sur les pins   
 display.lcd_clear();
 display.lcd_display_string("Attention! Point " , 1) # Affichage texte sur la 1ere ligne
 display.lcd_display_string( "de ReCUP plein !", 2) # Affichage texte sur la 2eme ligne
 
 
def badgeValide():
 sleep(0.01)# certaine fois ça place a cause d'une erreur sur les pins   
 display.lcd_clear();
 display.lcd_display_string("Badge valide " , 1) # Affichage texte sur la 1ere ligne
 
 
def analyse(stop_event, arg):
 sleep(0.01)# certaine fois ça place a cause d'une erreur sur les pins   
 display.lcd_clear();
 display.lcd_display_string("Patientez ...", 2) # Affichage texte sur la 2eme ligne
 str_pad =  " " * 16
 my_long_string = "  Tasse en cours d’analyse "
 my_long_string =  my_long_string

 while not stop_event.wait(1):
     for i in range (0, len(my_long_string)-15):
      lcd_text = my_long_string[i:(i+16)]
      display.lcd_display_string(lcd_text,1)
      sleep(0.3)
      display.lcd_display_string(str_pad,1)



def pasTasse(stop_event,arg):

 sleep(0.01)# certaine fois ça place a cause d'une erreur sur les pins	
	
 display.lcd_clear();
 display.lcd_display_string("Ceci n'est pas", 1)
 display.lcd_display_string("une tasse", 2)
 sleep(2)
 # Affichage texte sur la 2eme ligne

 while not stop_event.wait(1):
  
  
  
  display.lcd_clear();

  display.lcd_display_string("Deposez" , 1) # Affichage texte sur la 1ere ligne
  display.lcd_display_string("votre tasse", 2) # Affichage texte sur la 2eme ligne
  sleep(1)
  display.lcd_clear();
  display.lcd_display_string("Ou appuyez " , 1) # Affichage texte sur la 1ere ligne
  display.lcd_display_string("terminer", 2) # Affichage texte sur la 2eme ligne
  sleep(1)
  display.lcd_clear();





def nouvelleTasse(stop_event,arg):
 sleep(0.1)# certaine fois ça place a cause d'une erreur sur les pins
 display.lcd_clear();
 display.lcd_display_string("Tasse validee", 1)
 display.lcd_display_string("Merci !", 2)
 sleep(2)
 display.lcd_clear();
 display.lcd_display_string("Sinon=> Terminer", 2) # Affichage texte sur la 2eme ligne
 str_pad =  " " * 16
 my_long_string = "  Deposez une nouvelle tasse"
 my_long_string =  my_long_string

 while not stop_event.wait(1):
     for i in range (0, len(my_long_string)-15):
      lcd_text = my_long_string[i:(i+16)]
      display.lcd_display_string(lcd_text,1)
      sleep(0.3)
      display.lcd_display_string(str_pad,1)
   


def fin(stop_event,euro):
    
 display.lcd_clear();
 display.lcd_display_string("Caution rendue:", 1) # Affichage texte sur la 1ere ligne
 display.lcd_display_string( str(euro) +" euros", 2) # Affichage texte sur la 2eme ligne
 sleep(3)
 display.lcd_clear();
 display.lcd_display_string("Bonne Journee !" , 1)
 sleep(2)
 display.lcd_clear();
 
 
def timeout():
  display.lcd_clear();
  display.lcd_display_string("le temps attente", 1) # Affichage texte sur la 1ere ligne
  display.lcd_display_string("est depasse", 2) # Affichage texte sur la 2eme ligne
  sleep(3)
  display.lcd_clear();

 
