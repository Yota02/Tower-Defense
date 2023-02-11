# -*- coding: utf-8 -*-
"""
Created on Mon May 16 16:37:55 2022

@author: Alexis
"""

import tourelle as tr
Vitessemax=0.2
Vitessemin=0
Vie=10
base = 100
stopx = 475 
stopy = 420
liste_ovales = []

class Balle:
    global Vitessemax
    def __init__(self):
        """Fonction qui permet d'initialisé les valeur de la classe """
        self.rayon=10
        self.x=25
        self.y=25
        self.Vx=Vitessemax
        self.Vy=Vitessemin
        self.vie = 10
        self.base = 10
        self.liste_ovales = []

    def afficher(self,Can):
        """perme de crée un oval avec le tags Balle"""
        self.oval=Can.create_oval(self.x-self.rayon,self.y-self.rayon,self.x+self.rayon,self.y+self.rayon,fill='red', tags = "balle")
        self.liste_ovales.append(self.oval)
        
    def retirer(self, Can, i):
        """Permet de delete un oval"""
        global liste_ovales
        if len(liste_ovales) > 0 :
            self.oval=liste_ovales.pop(i)
            Can.delete(self.oval)

    def deplacement(self,dt):
        """ 
        Fonction qui permet de faire suivre le trajet des enemis
        """
        global Vmax
        if self.x>470 and self.y<30:
            self.Vx=Vitessemin
            self.Vy=Vitessemax
        elif self.x>470 and self.y<125 and self.y>120:
            self.Vx=-Vitessemax
            self.Vy=Vitessemin
        elif self.x<25 and self.y>120 and self.y<130:
            self.Vx=Vitessemin
            self.Vy=Vitessemax
        elif self.x<25 and self.y>220 and self.y<230:
            self.Vx=Vitessemax
            self.Vy=Vitessemin
        elif self.x>470 and self.x<475 and self.y>220 and self.y<225:
            self.Vx=Vitessemin
            self.Vy=Vitessemax
        elif self.x>470 and self.y<325 and self.y>320:
            self.Vx=-Vitessemax
            self.Vy=Vitessemin
        elif self.x<25 and self.y>320 and self.y<330:
            self.Vx=Vitessemin
            self.Vy=Vitessemax
        elif self.x<25 and self.y>420 and self.y<430:
            self.Vx=Vitessemax
            self.Vy=Vitessemin
            
    def deplacer(self,Can):
        """Fonction qui permet de faire déplacer l'oval"""
        Can.move(self.oval,self.Vx,self.Vy)
        self.x+=self.Vx
        self.y+=self.Vy

    def interaction(self,tourelle):
        """Fonction qui permet d'avoir une interaction avec la tourelle. 
        @distance : distance entre la balle et la tourelle"""
        global Vie
        distance=(( self.x-tourelle.x )**2+( self.y-tourelle.y )**2)**(1/2)
        while distance<100 and Vie>-1:
                Vie=Vie-2
                if Vie==0:
                    print("je suis mort")
                    
    def interaction2(self):
        while self.x != 474 and self.y != 420:
                if self.x >= 474 and self.x <= 475 and self.y == 420.0000000000676  :
                    print("cheeee t'as perdu")
                    self.base = base - 10
                    print(base)
            
             
          