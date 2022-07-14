import os
from colorama import Fore
from colorama import Style
from colorama import init

#init for colorama to fixed windows wierdness
init()

def print_yellow(s):
    print(Fore.YELLOW, Style.BRIGHT,s,Style.RESET_ALL)

def print_red(s):
    print(Fore.RED, Style.BRIGHT,s,Style.RESET_ALL)    

def print_blue(s):
    print(Fore.BLUE, Style.BRIGHT,s,Style.RESET_ALL)

def print_green(s):
    print(Fore.GREEN, Style.BRIGHT,s,Style.RESET_ALL)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
