import TFLite_detection_image_reCup
import cv2

from picamera import PiCamera
from time import sleep
import numpy as np


def detection_tasse():
    cam = cv2.VideoCapture(0)

    ret, img = cam.read()
    img = cv2.resize(img,(1024,768)) 



    cv2.imwrite('test1.jpg',img)


    cam.release()
    # # réglage de la résolution
    # camera.resolution = (1024,768)
    # 
    # # rotation de l'image (utile si la caméra est à l'envers)
    # camera.rotation = 180 
    # 
    # # aperçu, mais dans une portion de l'écran seulement
    # camera.start_preview(fullscreen = False, window = (50,50,640,480))
    # 
    # # un délai est nécessaire pour laisser le temps aux capteurs de se régler
    # sleep(5)
    # 
    # #on enregistre le fichier sur le bureau
    # camera.capture('test1.jpg')
    # 
    # #on fait disparaître l'aperçu.


    a = TFLite_detection_image_reCup.detection()
    print(" Le résultat est : ",a) 
    return a
