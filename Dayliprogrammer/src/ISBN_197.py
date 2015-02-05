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
    else:
        print("pas isbn")
   

