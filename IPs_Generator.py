import os
import time
import threading
from random import randint
from colorama import Fore, init

init(autoreset=True)

stop_loop = False

def vcolor(line):
    return line

logo = """

   ██████╗ ██╗  ██╗██╗███████╗██████╗ ███╗   ██╗
  ██╔═══██╗╚██╗██╔╝██║╚══███╔╝╚════██╗████╗  ██║
  ██║   ██║ ╚███╔╝ ██║  ███╔╝  █████╔╝██╔██╗ ██║
  ██║   ██║ ██╔██╗ ██║ ███╔╝   ╚═══██╗██║╚██╗██║
  ╚██████╔╝██╔╝ ██╗██║███████╗██████╔╝██║ ╚████║
   ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚═════╝ ╚═╝  ╚═══╝                                     
\t\t             IPs Generator
"""

colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
os.system(["clear", "cls"][os.name == 'nt'])
for line in logo.splitlines():
    print("".join(colors[randint(0, len(colors) - 1)] + vcolor(line)))
    time.sleep(0.05)

def dip_ipgen():
    while not stop_loop:
        a = randint(0, 255)
        b = randint(0, 255)
        c = randint(0, 255)
        d = randint(0, 255)
        evilmr = '{}.{}.{}.{}'.format(a, b, c, d)
        print(Fore.WHITE + "\t\t[" + Fore.BLUE + "+" + Fore.WHITE + "] Generated IP : " + Fore.RED + '| ' + Fore.GREEN + evilmr + Fore.RED + " | ")
        with open('Generated_IPs.txt', 'a') as file:
            file.write(evilmr + '\n')
        time.sleep(0.01)

def key_listener():
    input("Press Enter to stop generating IPs...")
    global stop_loop
    stop_loop = True

# Create and start threads
thread_generation = threading.Thread(target=dip_ipgen)
thread_input = threading.Thread(target=key_listener)

thread_generation.start()
thread_input.start()

thread_generation.join()
thread_input.join()
