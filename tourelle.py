# -*- coding: utf-8 -*-
"""
Created on Mon May 16 16:40:06 2022

@author: Alexis
"""


P=0
class Tourelle:
 
    def __init__(self):
        """Fonction qui permet d'initialisé les valeur de la classe """
        self.rayon=10
        self.x=0
        self.y=0
 
    def placers(self,Can):
        """Permet de placer des rectangle dans des zone donné"""
        if self.x<500 and self.y<50:
            print("terrain non approprié")
            P=1
        elif self.y>100 and self.y<150:
            print("terrain non approprié")
            P=1
        elif self.y>200 and self.y<250:
            print("terrain non approprié")
            P=1
        elif self.y>300 and self.y<350:
            print("terrain non approprié")
            P=1
        elif self.y>400 and self.y<450:
            print("terrain non approprié")
            P=1
        elif self.y>500 and self.y<550:
            print("terrain non approprié")
            P=1
        elif self.y<100 and self.y>50 and self.x<500 and self.x>450:
            print("terrain non approprié")
            P=1
        else:
            Can.create_rectangle(self.x-self.rayon,self.y-self.rayon,self.x+self.rayon,self.y+self.rayon,fill='black')
            print("placement de tourelle en x :", self.x,"y :", self.y)