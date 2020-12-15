import afficheur
import threading
import time
from reset_casier import thread_reset_casier
from petite_grande_tasse import thread_petite_grande_tasse
from bouton_terminer import thread_bouton_terminer
from time import sleep
from rfid import thread_rfid_lecture
from presence_tasse import thread_presence_tasse
import liberation_tasse
from presence_plateau import *
from bac_ouvert import *
from detection_tasse import detection_tasse
import requete_sql
import stockage
from presence_plateau_distri import *
 
from casier import Casier
from tasse import Tasse
from depose import *
import machine


timeout_depacé=False
bouton_terminé=False
tasse_présente=False
camera_dectection=0
#Les def sont des simulation qui seront remplacer par les retours actionneurs
#si la camera detecte la tasse ==> true
def cameraDetection():
    global camera_dectection
    if camera_dectection==1:
     camera_dectection=0  
     return False
     
    if camera_dectection==0:
     camera_dectection=1  
     return True
     
 

i=0
# simulation de depot de 3 objets avant que le bouton soit activé, ne fonctionne pas si on relance car la variable n'est pas initialisée a 0 à la fin


#la tasse est detecter dans la machine
# def tasseDetection():
#   sleep(3) # le temps de dépot de la tasse (a retirer)
#   return True

#evenement des thread
killb=threading.Event()
killp=threading.Event()
killa=threading.Event()
killn=threading.Event()
killf=threading.Event()
killbt=threading.Event()
killpt=threading.Event()
killpp=threading.Event()
killbo=threading.Event()
killt=threading.Event()
killrc=threading.Event()
killpgt=threading.Event()
#création des 3 casiers // doit se faire à l'init : créer une fonction ?
casier1 = Casier()
casier2 = Casier()
casier3 = Casier()



afficheur.stockage_init()
machine.init_machine()

# casier1.tofull_petites()
# casier1.tofull_grandes()
# casier2.tofull_petites()
# casier2.tofull_grandes()


##Test pour les affichage spécifique
##afficheur.bacOuvert()
##sleep(2)
##afficheur.plateauAbsent()
##sleep(2)
##afficheur.plein()
##sleep(2)

while True :
    sorti_ajout_tasse=False
    
    presence_plateau= thread_presence_plateau(killpp)
    bac_ouvert= thread_bac_ouvert(killbo)
    thread_bonjour = threading.Thread(target=afficheur.bonjour, args=(killb, "task"))

    euro=0
    thread_rfid = thread_rfid_lecture(killt)
    bac_ouvert.start()
    presence_plateau.start()
    thread_rfid.start()
    thread_bonjour.start()
    
    
    while True: #partie interrupteurs sécurités
         reset_casier = thread_reset_casier(killrc)
         sleep(0.1)
         reset_casier.start()  
         if (presence_plateau.result()): #plateau manquant
           if thread_rfid.isAlive():
               killt.set()
               killt.clear()
               killb.set() # on dit au thread affichage qu'il faut arreter
               sleep(0.5)
               thread_bonjour.join()
               killb.clear()
           afficheur.plateauAbsent()
           sleep(0.5)
##           thread_rfid = thread_rfid_lecture(killt)
##           thread_rfid.start()
          
         
        
         elif(bac_ouvert.result()):
             if thread_rfid.isAlive():
               killt.set()
               sleep(0.5)
               killt.clear()
               killb.set() # on dit au thread affichage qu'il faut arreter
               sleep(2)
               thread_bonjour.join()
               killb.clear()
             
             
             
             
             
##           thread_rfid = thread_rfid_lecture(killt)
##           thread_rfid.start()
             afficheur.bacOuvert()
             sleep(0.5)
        
             
         elif not stockage.check_capacity(casier1,casier2,casier3):
             if thread_rfid.isAlive():
               killt.set()
               sleep(0.5)
               killt.clear()
               killb.set() # on dit au thread affichage qu'il faut arreter
               sleep(2)
               thread_bonjour.join()
               killb.clear()
             afficheur.plein()
             sleep(2)
             
           
         
      
           
         elif (not bac_ouvert.result() and not presence_plateau.result() ):
          sleep(0.5)
          if not thread_rfid.isAlive() and not thread_bonjour.isAlive():
              thread_rfid = thread_rfid_lecture(killt)
              thread_rfid.start()
          
          if not thread_bonjour.isAlive():
           thread_bonjour = threading.Thread(target=afficheur.bonjour, args=(killb, "task"))
           thread_bonjour.start()
          
          if not thread_rfid.isAlive() and thread_bonjour.isAlive():
             break
            
            
         result_casier=reset_casier.result()
         
         if result_casier and bac_ouvert.result():
                 casier1.clear()
                 casier2.clear()
                 casier3.clear()
                 print('init')
                 afficheur.reset_casier()
          
        
       
        
    killrc.set()
    killpp.set()
    presence_plateau.join()
    killpp.clear()
    killbo.set()
    bac_ouvert.join()
    killbo.clear()
    killt.clear()
    killrc.clear()
    
    
   
    id_badge=thread_rfid.result()     
    thread_rfid.join() # on attends que le threads rfid soit fini ( que un badge soit detecter) pour continuer
    
    
 

    killb.set() # on dit au thread affichage qu'il faut arreter
    thread_bonjour.join()
    killb.clear()#on annule la demande pour la prochaine boucle
    
    
    if not requete_sql.identification_sql(id_badge):
        afficheur.badge_invalide()
        sleep(2)
    else:
        
            
        afficheur.badgeValide()
        sleep(3)
        afficheur.deposeTasse() # on afficher le message pour inviter l'utilsateur a deposer sa tasse
       

        x=0
        boutonTerminer= False
        presence_tasse = thread_presence_tasse(killpt)
        presence_tasse.start()
        
        
        
        debut= time.time()# servira pour le timer de fin automatique
        
        while True: #tant que le bouton terminer n'est pas actionner on continu
         #ajouter un thread bouton terminer qui finira le programme a tout
         sleep(0.1)
         if x==0 and (time.time()-debut>=30) :
               killpt.set()
               presence_tasse.join()
               killpt.clear()
               afficheur.timeout()
               break
              
         if tasse_présente==True or presence_tasse.result(): #si la tasse est detecter
           analyse = threading.Thread(target=afficheur.analyse, args=(killa, "task"))
           timeout_depacé=False
           bouton_terminé=False
           tasse_présente=False

           
           if x==2: # permet de kill le threads pas de tasse si il a ete activé
             killp.set()
             thread_pas_tasse.join()
             killp.clear()
             thread_terminer.join()
             killbt.clear()
             
           if x==1: # permet de kill le threads nouvelle tasse si il a ete activé
            killn.set()
            nouvelleTasse.join()
            killn.clear()
            thread_terminer.join()
            killbt.clear()
            
            if x==0:
               killpt.set()
               presence_tasse.join()
               killpt.clear()
            
           #afficheur.fermeTrappe()#message fermer la trappe
           #sleep(2) #simuler la fermeture( a retirer) a remplacer par capteur trappe
    #        cameraDetection() # on change la valeur de camera detection pour simuler quelqu'un qui met un pierre un coup sur 2 (a retirer)
           analyse.start() #on affiche que la tasse est en analyse
           sleep(2) # le temps permet de simuler un vrai analyse (a retirer)
           tasse = detection_tasse()
           if tasse: # la camera a bien detecter une tasse
             
            
             
             
             killa.set() # on dit au thread de stopper l'affichage analyse
             analyse.join() # on attends que le thread est bien fini
             killa.clear() # on remet l'evenement a 0
             
             if not stockage.check_capacity(casier1,casier2,casier3):
                 afficheur.plein()
                 sleep(2)
                 break
             petite_grande_tasse=thread_petite_grande_tasse(killpgt)
             petite_grande_tasse.start()

             presence_plateau_distri()
              
             liberation_tasse.liberer_tasse()
             if petite_grande_tasse.result():
               tasse_o = Tasse()
               killpgt.set()
             else:
               tasse_o = Tasse()
               tasse_o.to_petite()
               killpgt.set()
               
               
               
               
              # si petit alors to_petite()
             thread_distribution = threading.Thread(target=stockage.stockage(tasse_o,casier1,casier2,casier3))
             thread_distribution.start()
             killpgt.clear()
              
             
             
             if requete_sql.ajout_tasse_sql(id_badge):
                 euro= euro+2 # on ajoute les sous sous
             thread_terminer = thread_bouton_terminer(killbt)
             thread_terminer.start()
             presence_tasse = thread_presence_tasse(killpt)
             presence_tasse.start()
             
             
             
             nouvelleTasse= threading.Thread(target=afficheur.nouvelleTasse, args=(killn, "task"))
             nouvelleTasse.start()
             sleep(1)

             
             x=1 #dire que le thread nouvelle tasse est activé afin de le retirer plus tard
                
                
           elif not tasse:
             x=2 #dire que le thread pas tasse est activé afin de le retirer plus tard
             killa.set()  # on dit au thread de stopper l'affichage analyse
             analyse.join() # on attends que le thread est bien fini
             killa.clear()# on remet l'evenement a 0
             thread_terminer = thread_bouton_terminer(killbt)
             thread_terminer.start()
             presence_tasse = thread_presence_tasse(killpt)
             presence_tasse.start()
             sleep(0.5)
             thread_pas_tasse = threading.Thread(target=afficheur.pasTasse, args=(killp, "task"))
             thread_pas_tasse.start()
             
            
           debut=time.time()
         
           while not (bouton_terminé==True or tasse_présente==True or timeout_depacé==True):
            sleep(0.01)  #eviter le lag
            if (time.time()-debut>=30):
             timeout_depacé=True
            elif thread_terminer.result():
             bouton_terminé=True
            elif presence_tasse.result():
             tasse_présente=True
              
           if x==1:   
               killn.set()
               nouvelleTasse.join()
               killn.clear()
          
           if x==2:
               killp.set()
               thread_pas_tasse.join()
               killp.clear()
               
               
           if bouton_terminé==True: #si bouton terminer on break la boucle principal et on repasse à une demande de badge
               killbt.set()
               thread_terminer.join()
               killbt.clear()
               killpt.set()
               presence_tasse.join()
               killpt.clear()
               break
            
           if timeout_depacé==True: # time out
               killbt.set()
               thread_terminer.join()
               killbt.clear()
               killpt.set()
               presence_tasse.join()
               killpt.clear()
               afficheur.timeout()
               print("timeout")
               break
            
           if tasse_présente==True:# on ferme les thread et on rebouclez sur une demande de tasse
               killbt.set()
               thread_terminer.join()
               killbt.clear()
               killpt.set()
               presence_tasse.join()
               killpt.clear()
               
               
         
         
          
    
        
     

    fin = threading.Thread(target=afficheur.fin, args=(killf,euro))
    fin.start()
    fin.join()
    i=0
    
    
