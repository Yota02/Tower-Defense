# -*- coding: utf-8 -*-
"""
@author: Alexis
"""

from tkinter import *
from PIL.Image import*
from PIL import Image, ImageTk
from PIL import ImageTk as itk
from importlib import reload
import numpy as np
import balle as bl
import tourelle as tr
import time
from tkinter.messagebox import *
 
reload(bl)
reload(tr)
Largeur = 500
Hauteur = 500
budget=300.0
T=[]
listBalle=[]
S=0
i=0

def Jeu():
    """Permet de faire fonctionné le jeu, et lancé par le bouton 'jouer'. Une fois lancer fait apparaitre une balle et la fait se déplacer """
    global budget
    global T
    for i in range(1):
        balle = bl.Balle()
        listBalle.append(balle)
        balle.afficher(Can)
        dt=0.6
    while 1:
        print(balle.liste_ovales)
        for balle in listBalle:
            fenetre.update()
            balle.deplacement(dt)
            balle.deplacer(Can)
            game_over(balle.base)
            for tourelle in T:
                balle.interaction(tourelle)
                balle.interaction2()   
                balle.retirer(Can)
                
def Placer(event):
    """Permet d'appeller la class Tourelle et ainsi de placer les tourelles au pointeur, si le budget et sufisant"""
    global budget
    global T
    for i in range(1):
        tourelle1 = tr.Tourelle()
        T.append(tourelle1)
    for tourelle1 in T:
            tourelle1.x=event.x
            tourelle1.y=event.y
    if budget>19.9:
                tourelle1.placers(Can)
                budget=budget-20
    else:
                 print("pas assez d'argent il vous manque", 20 - budget)
                 

def argent():
  """permet d'afficher le budget"""
  print("votre dudget est de", budget, "$")
  
def game_over(viebase):
    """fait une alerte si vie base arrive 0"""
    if viebase == 0:
       showinfo("Game over", "Vous avez perdu")
    
    
fenetre = Tk()
fenetre.title('Waifu krieg marine')

Can = Canvas(fenetre, width = Largeur, height =Hauteur, bg ="white")
Can.pack()

bouton1=Button(fenetre, text="Jouer",command=Jeu)
bouton1.pack()
bouton2=Button(fenetre, text="argent",command=argent)
bouton2.pack()
 
Can.bind('<Button-1>', Placer)
Can.pack()

image3 = Image.open("base.png")
resize_image3 = image3.resize((141, 461))
base = ImageTk.PhotoImage(resize_image3)

Can.create_rectangle((0,0), (500,50), fill='grey')
Can.create_rectangle((0,50), (500,100), fill='blue')
Can.create_rectangle((0,100), (500,150), fill='grey')
Can.create_rectangle((0,150), (500,200), fill='blue')
Can.create_rectangle((0,200), (500,250), fill='grey')
Can.create_rectangle((0,250), (500,300), fill='blue')
Can.create_rectangle((0,300), (500,350), fill='grey')
Can.create_rectangle((0,350), (500,400), fill='blue')
Can.create_rectangle((0,400), (500,450), fill='grey')
Can.create_rectangle((0,450), (500,500), fill='blue')
Can.create_rectangle((450,50), (500,100), fill='grey')
Can.create_rectangle((0,150), (50,200), fill='grey')
Can.create_rectangle((450,250), (500,300), fill='grey')
Can.create_rectangle((0,350), (50,400), fill='grey')
Can.create_image(475,450, image=base)

fenetre.mainloop()