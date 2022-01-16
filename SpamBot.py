import pyautogui, time, os
from tqdm import tqdm
import time
import sys

def Spam():
    time.sleep(5)
        
    for i in tqdm(range(menge)):
        
        pyautogui.typewrite(wert)
        pyautogui.press('enter')
        time.sleep(0.25)
        print("\rAnzahl: %i" % i+" ")
        
    

print('''
##############
###SPAM BOT###      -By Marco Gamberale
##############''')
print("")

time.sleep(2)

wert = input("Message = ")
menge = int(input("Count = "))

print("Ready!")
time.sleep(1)
print("Open your chat website, and click on your chat partner and stay.")
print("")
time.sleep(2)

for i in range(10, 0, -1):
    print("It begins in: "+str(i))
    time.sleep(1)

print("")
os.system("cls")

Spam()

print("")
input('Press "Enter", to leave.. ')


