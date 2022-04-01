#    Copyright (C) 2022  Owen2k6
#    Do not modify this code

#    You have no need to modify this code.
#    This file is here to allow you to seemlessly update the data to the next version.
#    Modifying this code MAY lead to issues with the data.
#    Please DO NOT modify anything within this file. As it most likely WILL mess up any stored data.
#    Im looking at you kyle. you'll fuck smth up i know it XD

# Start Updater check
import system
from urllib.request import urlopen

URL = "https://api.owen2k6.com/O2K6LV.txt"
HTM = urlopen(URL).read()
LTS = str(HTM)
FNL = LTS.replace('b', '')
FN2 = FNL.replace("'", "")
FN3 = float(FN2)

VER = system.VER
if FN3 == VER:
  print("Owen2k6 Launcher is up to date.")
if FN3 > VER:
  print("Owen2k6 Launcher is outdated. update all O2k6L files to make sure the updater works correctly.")
  print("The updater WILL still update your data, however it is not the latest versio of Owen2k6 Launcher.")
  print(f"Your System Version is marked as V{VER}")
  print(f"The latest version that the server lists is {FN3}")
if FN3 < VER:
  print("Your System data is incorrect. O2k6L System code has been modified in a way that prevents the data from updating correctly.")
  print("Reminder that modifying O2k6L code is against the GNU licence agreement.")
  print("We allow the modification of Main.py for adding your py apps in. But modifying anything else is against our licence")