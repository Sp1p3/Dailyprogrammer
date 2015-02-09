# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "canillas"
__date__ = "$6 fevr. 2015 20:11:56$"

import pixel


if __name__ == "__main__":
    print("Hello World")
    
def coeur():
    coeurX=[1,1,2,2,2,3,3,3,4,4,4,5,5]
    coeurY=[1,2,1,2,3,2,3,4,1,2,3,1,2]
    pixel.initialiser(7,7,10)
    pixel.couleur()
    for x in range(len(coeurX)):
        pixel.marquer(coeurX[x],coeurY[x])
        pixel.afficher(0.1)
    pixel.afficher()

#lettre de l'alphabet en 3 par 5 
#trouver une methode plus pros qu'hardcoder les coordonnées à la main 
    
def  lettreA():
    #affiche la lettre A dans un maillage de 3 par 5 
    lettreAX=[0,0,0,0,1,1,2,2,2,2]
    lettreAY=[1,2,3,4,0,2,1,2,3,4]
    pixel.initialiser(3,5,10)
    for x in range(len(lettreAX)):
        pixel.marquer(lettreAX[x],lettreAY[x])
    pixel.afficher()    
    
    

def  lettreB():
    #affiche la lettre B dans un maillage de 3 par 5 
    lettreBX=[0,0,0,0,0,1,1,1,2,2]
    lettreBY=[0,1,2,3,4,0,2,4,1,3]
    pixel.initialiser(3,5,10)
    for x in range(len(lettreBX)):
        pixel.marquer(lettreBX[x],lettreBY[x])
    pixel.afficher()    
    
    
 
def  lettreA():
    #affiche la lettre A dans un maillage de 3 par 5 
    lettreAX=[0,0,0,0,1,1,2,2,2,2]
    lettreAY=[1,2,3,4,0,2,1,2,3,4]
    pixel.initialiser(3,5,10)
    for x in range(len(lettreAX)):
        pixel.marquer(lettreAX[x],lettreAY[x])
    pixel.afficher()    
    
       
def pixel_lecture():
    return 0 

def pixel_afficher():
    return 0 

    
    