# Code By ChokunPlayZ
# Completely Open-Sorce Edit it to whatever you want

import time
import pyautogui

Script1 = "scripts/1.txt"
Script2 = "scripts/2.txt"
Script3 = "scripts/3.txt"
Script4 = "scripts/4.txt"
Script5 = "scripts/5.txt"
Script6 = "scripts/6.txt"
Script7 = "scripts/7.txt"
Script8 = "scripts/8.txt"
Script9 = "scripts/9.txt"
Script10 = "scripts/10.txt"

def Sendlines():
    print(" ")
    print(" ")
    print("Starting")
    time.sleep(2)
    print("Fuck em")
    with open(Script) as f:
        lines = f.readlines()
    for line in lines:
        pyautogui.typewrite(line.strip())
        pyautogui.press('enter')
        print("sent : " + line)

def SendWords():
    print(" ")
    print(" ")
    print("Starting")
    time.sleep(2)
    print("Fuck em")
    with open(Script) as f:
        lines = f.readlines()
        for line in lines:
            for word in line.split(" "):
                pyautogui.typewrite(word)
                pyautogui.press('enter')
                print("sent : " + word)

print("Select an Option")
print("1. Spam Line By Lines")
print("2. Spam Words By Words")
print()
opt = input ("Select : ")

time.sleep(1)

print("Select a File")
print("enter a number")
print("the file name should be number")
print("UP to 10")
print("1 is a default file")
print()
sf = input ("File Number : ")

if (sf == "1"):
    print("1 is selected")
    Script = Script1
elif (sf == "2"):
    print("2 is selected")
    Script = Script2
elif (sf == "3"):
    print("3 is selected")
    Script = Script3
elif (sf == "4"):
    print("4 is selected")
    Script = Script4
elif (sf == "5"):
    print("5 is selected")
    Script = Script5
elif (sf == "6"):
    print("6 is selected")
    Script = Script6
elif (sf == "7"):
    print("7 is selected")
    Script = Script7
elif (sf == "8"):
    print("8 is selected")
    Script = Script8
elif (sf == "9"):
    print("9 is selected")
    Script = Script9
elif (sf == "10"):
    print("10 is selected")
    Script = Script10
else:
    print("File Name is invald")
    print("Quitting ..")
    quit()

if (opt == "1"):
    print("Option Selected : 1")
    Sendlines()
elif (opt == "2"):
    print("Option Selected : 2")
    SendWords()
else:
    print("invald input quiting")
    quit()

print()
print("Done!")
print("Quitting..")
time.sleep(2)
quit()