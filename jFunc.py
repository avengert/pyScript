"""

	Commonly written functions by me to use in all my scripts.

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
	if int(sys.version[0]) > 2:
        	return True
	else:
		return False

# A way to make a border around text.
def pprint(i=""):
    j = "=" * len(i)
    print(j + "\n\n" + i + "\n\n" + j)

# A way to pause the screen making you press [Enter] before moving forward.
def pause(i="Press [Enter] to Continue"):
    if(getPyVer()):
        input(i)
    else:
        raw_input(i)