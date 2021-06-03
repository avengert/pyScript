"""

	Commonly written functions by me to use in all my scripts.
	Version 0.0.2
	Update:
		06/03/2021: Changed pprint to use version 3.6 formatting with the print code. Adding pprint ability to change border style and length.

"""
import os, datetime, sys, platform

def clear():
    if getOS():  # if Windows
        os.system("cls")
    else:
        os.system("clear")

def getOS():
    if platform.system() == "Windows":
        return True
    else:
        return False

def getPyVer():
    if int(sys.version[0]) > 2: # Detects Python version and returns True if it is greater than 2
        return True
    else:
        return False

# A way to make a border around text.
def pprint(i="", s="=", l=30): # Add ability to enter style, and length.
    j = s * len(i)
    if(len(j)>l): 
        j = s * l
        if(getPyVer()): # If running Python 3+ then this section runs.
            print(f"{j}\n\n{i}\n\n{j}")
        else:
            print(j + "\n\n" + i + "\n\n" + j)
    else:
        if(getPyVer()): # If running Python 3+ then this section runs.
            print(f"{j}\n\n{i}\n\n{j}")
        else:
            print(j + "\n\n" + i + "\n\n" + j)

# A way to pause the screen making you press [Enter] before moving forward.
def pause(i="Press [Enter] to Continue"):
    if(getPyVer()):
        input(i)
    else:
        raw_input(i)
