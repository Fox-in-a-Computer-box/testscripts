# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 18:32:24 2017

@author: FURBUTT
"""

'''
definitions
'''

dict = {"user":"admin"}

def createacc(x,y):
    dict[x] = y
    return

def loginacc(x,y):
    if y == dict[x]:
        print("you have logged in")
        
    else:
        print("the credentials you have entered are invalid")
        
'''
code
'''

while True:
    inpt = input("do you wish to 'create' an account or 'login' or 'exit'?")
    
    if inpt == 'login':
        usrname = input("please put in your username")
        psswrd = input("please put in your password")
        loginacc(usrname,psswrd)
        
    elif inpt == 'create':
        crtusrname = input("create a username")
        crtpsswrd = input("create a password")
        createacc(crtusrname,crtpsswrd)
        
    else:
        break

print('goodbye')