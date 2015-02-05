# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "canillas"
__date__ = "$5 fevr. 2015 10:50:25$"



    
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
   

if __name__ == "__main__":
    
        
    print("Hello 197")
    tab= [0,7,4,7,5,3,2,6,9,9]
    CheckIsbn(tab)
    tab=[0,5,4,5,0,1,0,2,2,5]
    CheckIsbn(tab)
    
    