#------------- IMPORT ------------#
from os import system as c
import time
import random

#------------- COLOUR ------------#
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
B = '\x1b[38;5;51m'
P = '\x1b[38;5;201m'

#------------- PAID KEY -------------#
paid_key = "VIPDIAMOND2025"

#------------- LOGO -------------#
def logo():
    c('clear')
    print(f"""{R}
██████╗ ██╗ █████╗ ███╗   ███╗███████╗██╗███╗   ██╗ ██████╗ 
██╔══██╗██║██╔══██╗████╗ ████║██╔════╝██║████╗  ██║██╔════╝ 
██████╔╝██║███████║██╔████╔██║█████╗  ██║██╔██╗ ██║██║  ███╗
██╔═══╝ ██║██╔══██║██║╚██╔╝██║██╔══╝  ██║██║╚██╗██║██║   ██║
██║     ██║██║  ██║██║ ╚═╝ ██║███████╗██║██║ ╚████║╚██████╔╝
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
{G}                 HACKING WORLD - VIP DIAMOND TOOL
{A}--------------------------------------------------
""")

#------------- PAID CHECK -------------#
def paid_check():
    logo()
    print(f"{Y}This is a VIP Paid Tool. You need an Activation Key to use this.")
    key = input(f"{C}Enter Your Paid Activation Key: ")
    if key != paid_key:
        print(f"\n{R}[!] Invalid Key! Purchase VIP Access First.")
        time.sleep(2)
        exit()
    else:
        print(f"\n{G}[✓] Access Granted! Welcome to Diamond Hack VIP Tool!")
        time.sleep(2)
        menu()

#------------- MAIN MENU -------------#
def menu():
    logo()
    print(f"{A}[1] START DIAMOND HACK")
    print(f"{A}[2] EXIT TOOL")
    print(f"{A}--------------------------------------------------")
    choice = input(f"{Y}[?] SELECT OPTION: ")
    if choice == '1':
        diamond_hack()
    elif choice == '2':
        exit()
    else:
        print(f"{R}[!] INVALID OPTION, TRY AGAIN")
        time.sleep(1)
        menu()

#------------- DIAMOND HACK -------------#
def diamond_hack():
    logo()
    c('espeak "Starting VIP Free Fire Diamond Hack"')
    uid = input(f"{C}Enter Free Fire UID: ")
    print(f"\n{Y}[+] Connecting to VIP Server for UID {uid}...")
    time.sleep(3)
    print(f"{G}[✓] UID Verified!")
    time.sleep(1)
    print(f"{B}[+] Selecting Diamond Packages...\n")
    time.sleep(2)

    amounts = [500, 1000, 2000, 5000, 10000, 20000]
    for amount in amounts:
        print(f"{C}[*] Injecting {amount} Diamonds...")
        time.sleep(1)

    print(f"\n{R}[!] Root Verification Failed!")
    print(f"{Y}This tool is for Rooted Devices only.")
    time.sleep(2)
    print(f"{G}Please Root your device and try again.\n")
    input(f"{A}Press Enter to Exit...")
    exit()

#------------- START TOOL -------------#
paid_check()