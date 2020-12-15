# -*- coding: utf-8 -*-

import random

from casier import Casier
from tasse import Tasse
from depose import *


#doit retourner true s'il reste de l'espace pour mini 1 grande et 1 petite tasse, retourne false sinon
def check_capacity(casier1,casier2,casier3):
    if (casier1.full_grandes == False or casier2.full_grandes == False or casier3.full_grandes == False) and (casier1.full_petites == False or casier2.full_petites == False or casier3.full_petites == False ):
        return True
    else:
        return False
    
def stockage(tasse,casier1,casier2,casier3):
    #Si tasse petite
    if tasse.grande == False:
        
        if casier1.full_petites == False:
            
            if casier1.p1 <= 4:
                print("stockage tasse c1, p1")
                
                thread = threading.Thread(target=depose("c1","p1"))
                thread.start()
                thread.join()
                
                casier1.add_tasse_p1()
                
                
            elif casier1.p2 <= 4:
                print("stockage tasse c1, p2")
                
                thread = threading.Thread(target=depose("c1","p2"))
                thread.start()
                thread.join()
                
                casier1.add_tasse_p2()
                if casier1.p2 == 5:
                    casier1.tofull_petites()
                
        elif casier2.full_petites == False:
            if casier2.p1 <= 4:
                print("stockage tasse c2, p1")
                
                thread = threading.Thread(target=depose("c2","p1"))
                thread.start()
                thread.join()
                
                casier2.add_tasse_p1()
                
            elif casier2.p2 <= 4:
                print("stockage tasse c2, p2")
                
                thread = threading.Thread(target=depose("c2","p2"))
                thread.start()
                thread.join()                
                
                casier2.add_tasse_p2()
                if casier2.p2 == 5:
                    casier2.tofull_petites()
                    
        elif casier3.full_petites == False:
            if casier3.p1 <= 4:
                print("stockage tasse c3, p1")
                
                thread = threading.Thread(target=depose("c3","p1"))
                thread.start()
                thread.join()                
                
                casier3.add_tasse_p1() 
            elif casier3.p2 <= 4:
                print("stockage tasse c3, p2")
                
                thread = threading.Thread(target=depose("c3","p2"))
                thread.start()
                thread.join()                
                
                casier3.add_tasse_p2()
                if casier3.p2 == 5:
                    casier3.tofull_petites()
        else:
            print("plus de place petites tasses")
            
            
    #Si tasse grande 
    elif tasse.grande == True:
        
        if casier1.full_grandes == False:
            if casier1.g1 <= 3:
                print("stockage tasse c1, g1")
                
                thread = threading.Thread(target=depose("c1","g1"))
                thread.start()
                thread.join()
                
                casier1.add_tasse_g1()
            elif casier1.g2 <= 3:
                print("stockage tasse c1, g2")
                
                thread = threading.Thread(target=depose("c1","g2"))
                thread.start()
                thread.join()                
                
                
                casier1.add_tasse_g2()
                if casier1.g2 == 4:
                    casier1.tofull_grandes()
                
        elif casier2.full_grandes == False:
            if casier2.g1 <= 3:
                print("stockage tasse c2, g1")
                
                thread = threading.Thread(target=depose("c2","g1"))
                thread.start()
                thread.join()                        
                
                casier2.add_tasse_g1()
                
            elif casier2.g2 <= 3:
                print("stockage tasse c2, g2")
                
                thread = threading.Thread(target=depose("c2","g2"))
                thread.start()
                thread.join()                       
                
                casier2.add_tasse_g2()
                if casier2.g2 == 4:
                    casier2.tofull_grandes()
                    
        elif casier3.full_grandes == False:
            if casier3.g1 <= 3:
                print("stockage tasse c3, g1")
                
                thread = threading.Thread(target=depose("c3","g1"))
                thread.start()
                thread.join()                  
                
                casier3.add_tasse_g1() 
            elif casier3.g2 <= 3:
                print("stockage tasse c3, g2")
                casier3.add_tasse_g2()
                
                thread = threading.Thread(target=depose("c3","g2"))
                thread.start()
                thread.join()                  
                
                if casier3.g2 == 4:
                    casier3.tofull_grandes()
        else:
            print("plus de place grandes tasses")






#test avec de multiples tasses, grandes ou petites
# for i in range(60):
#     tasse = Tasse()   
#     r = random.randrange(0,2)
#     print(check_capacity())
#     if r == 1:
#         tasse.to_petite()
#         if check_capacity() == True:
#             stockage(tasse)
#     else:
#         if check_capacity() == True:
#             stockage(tasse)
    

# tasse = Tasse() 
# # tasse.to_petite()
# stockage(tasse)
# 
# tasse = Tasse() 
# tasse.to_petite()
# stockage(tasse)


# tasse = Tasse() 
# tasse.to_petite()
# stockage(tasse)