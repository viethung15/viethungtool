import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd Infect && bash src/Logo.sh")

print("  \033[1;34m[1] >> \033[1;36;40mInfect")
print("  \033[1;34m[2] >> \033[1;36;40mExit")

chon = str(input('InfEct:'))

if chon == "1":
 os.system("clear")
 os.system("cd && cd Infect && python2 src/InfectMenu.py")
elif chon == "2":
 time.sleep(0.1)
 print("\033[1;31;40mVui lòng chờ.....")
 os.system("cd")
else:
 print("\033[1;31;40mInvalid input. Reloading Tool") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd Infect")
 os.system("bash install.sh")
