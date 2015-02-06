# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "canillas"
__date__ = "$5 fevr. 2015 10:50:25$"
import ISBN_197
import FLOOD_200
import random
import pixel




    


if __name__ == "__main__":
    
        
    print("Hello 197 DONE")
    #tab= [2,2,2,2,2,2,2,2,2,2]
    #print(len(tab))
    #ISBN_197.CheckIsbn(tab)
    #print(int(random.random()*100))
    #print(ISBN_197.GenerateIsbn())
    #print(ISBN_197.GenerateIsbn())
    print("Hello 200 DOING")
    FLOOD_200.hello()
    
    print ("dessine des coeurs avec pixel")
#    pixel.initialiser(30,30,20)
    
#    print("largeur: ",pixel.largeur)
#    print("hauteur: ",pixel.hauteur)
#    for x in range(pixel.largeur):
        
#        pixel.marquer(x,x)
#        pixel.afficher(1)
#    pixel.afficher()
   
    coeurX=[1,1,2,2,2,3,3,3,4,4,4,5,5]
    coeurY=[1,2,1,2,3,2,3,4,1,2,3,1,2]
    pixel.initialiser(7,7,10)
    pixel.couleur()
    for x in range(len(coeurX)):
        pixel.marquer(coeurX[x],coeurY[x])
        pixel.afficher(0.1)
    pixel.afficher()
    
    