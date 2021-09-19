"""
Preloaders
-----------------
Create colored preloaders and animations in your console.
NOTE: Doesn't work in IDLE.
"""
import os
import time

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
UNDERLINE = '\033[4m'
END = '\033[0m'

animations = {
    "default-loader": [f"{CYAN}[=      ]{END}", f"{CYAN}[==     ]{END}", f"{CYAN}[===    ]{END}",
                       f"{CYAN}[=====  ]{END}", f"{CYAN}[======]{END}", f"{CYAN}[ ====]{END}",
                           f"{CYAN}[  ===]{END}", f"{CYAN}[   ==]{END}", f"{CYAN}[    =]{END}"]
    }
def show_loader(animation, waiting, loops):
    os.system("")
    if isinstance(animation, str):
        animation = animations[animation]
    for x in range(loops):
        print(animation[x % len(animation)], end="\r")
        time.sleep(waiting)
if __name__ == "__main__":
    print("=== Preloaders ===\n")
    time.sleep(0.5)
    show_loader("default-loader", 0.2, 100)
    
