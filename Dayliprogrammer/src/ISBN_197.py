#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "canillas"
__date__ = "$5 fevr. 2015 10:52:12$"
import random 

def CheckIsbn(tab):
    somme=0
    j=len(tab)
    for i in tab:
        somme=somme+(i*j)
        j=j-1
    
    if ((somme % 11) == 0 ):
        print("isbn")
        return 0
    else:
        print("pas isbn")
        return 1
  
 #on brute-force le contenu de la cl�es puis on v�rifie  
   
def GenerateIsbn():
    isbn=[0]*10
    isbn[1] = 1 
    while(CheckIsbn(isbn) != 0 ): 
        print(isbn)
        i=0
        while i < len(isbn):
            isbn[i]=int(random.random()*10)
            i=i+1
    
    
    return isbn   

#la valeur max d'une la somme de verification d'un isbn est de 55*9 (495)
#on peut generer une somme de verification et r�partir les valeurs dans l'ordre 
# de la cl�es ou le d�sordre

