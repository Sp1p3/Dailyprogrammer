#! /usr/bin/python

# 
# http://www.reddit.com/r/dailyprogrammer/comments/2vc5xq/20150209_challenge_201_easy_counting_the_days/
# 
# l'idée est de fournir une date et de compté le nombre de jour a partir de la date locale  
__author__ = "canillas"
__date__ = "$11 fevr. 2015 11:56:27$"

import time

def hello():
    print("hello")
    print(time.clock())
    print(time.localtime().tm_mon)
    print(time.time())