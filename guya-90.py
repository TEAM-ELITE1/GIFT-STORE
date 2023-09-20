#crete tools
import os
import sys
import time
import marshal
import base64
import datetime
import uuid

logo2="""\033[92;1m Author  : TOM CHOWDHURY 
 Github  : TOM-CHOWDHUARY
 Facebook: ALEX RAFI CHOWDHURY 
 Tools   : PAID
 Version : 2.0.6"""
logo="""
\033[92;1m
 ██████ ██    ██ ██████  ███████ ██████  
██       ██  ██  ██   ██ ██      ██   ██ 
██        ████   ██████  █████   ██████  
██         ██    ██   ██ ██      ██   ██ 
 ██████    ██    ██████  ███████ ██   ██"""
                              
os.system("clear")
os.system("clear")
print(logo)
print(54*"=")
print(logo2)
print(54*"=")
print(" ")
print('\033[97;1m [1] FOLLOW ME ON FB')
print('\033[97;1m [2] EXIT')
opt = input('\n   Choose option >>> ')
if opt == '1':
	os.system('xdg-open https://www.facebook.com/mdrakib.rayhan.904?mibextid=ZbWKwL')
else:
	exit()
   
os.system("clear")
print(logo)
print(108*"=")
print(logo2)
print(108*"=")         
print(" [1] file cloning")
print(" [2] random")
print(" [0] exit")
print(108*"=")
ariyan=input(" \033[93;1m[√] CHOOSE :")
if ariyan in ["1","01"]:
	
	os.system("clear")
	
	from random import *

print(logo)
print(108*"=")
print(logo2)
print(108*"=")
print(" ")
user_password=input(" [★] TARGET PASSWORD :")
password=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]

guess=""

while(guess!=user_password):
	guess=""
	for letter in range(len(user_password)):
		guess_letter=password[randint(0,25)]
		guess=str(guess_letter)+str(guess)
		print(guess)
		
		
print("Your correct password is :", guess)
	


