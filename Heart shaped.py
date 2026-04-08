import math
import time
import os

# Enable ANSI colors on Windows
os.system("")

def heart():
    for y in range(15, -15, -1):
        line = ""
        for x in range(-30, 30):
            formula = (x*0.05)**2 + (y*0.1)**2 - 1
            heart_shape = formula**3 - (x*0.05)**2 * (y*0.1)**3
            
            if heart_shape <= 0:
                # Center text
                if -1 < y < 1 and -10 < x < 10:
                    text = "XXXXXXXXXXXXXX"
                    index = (x + 10) // 4
                    if 0 <= index < len(text):
                        line += text[index]
                    else:
                        line += " "
                else:
                    line += "*"
            else:
                line += " "
        
        print("\033[91m" + line + "\033[0m")

while True:
    os.system("cls")
    heart()
    time.sleep(1)