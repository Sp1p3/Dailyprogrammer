# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "canillas"
__date__ = "$5 fevr. 2015 10:50:25$"


if __name__ == "__main__":
    print("Hello 197")
    somme=0
    j=0
    tab = [0,7,4,7,5,3,2,6,9,9]
    
    for i in tab:
        j=j+1
        somme=somme+(i*j)
    
    print(somme)
    if ((somme % 11) == 0 ):
        print("isbn")
    else:
        print("pas isbn")