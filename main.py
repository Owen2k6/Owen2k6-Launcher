#    Copyright (C) 2022  Owen2k6
#    Do not modify this code
from replit import db
print("Owen2k6 Launcher V0.5")
print("Copyright (C) 2022 Owen2k6")

# ADMIN DB RESET. DO NOT TOUCH.
# db["RUNINNIT"] = int(0)
# END OF ADMIN. DO NOT UNCOMMENT IF ALREADY SET UP.

# ADMIN LOADER. DO NOT REMOVE OR COMMENT
RUNINT = int(db["RUNINNIT"])
RUN = False
# END OF ADML.

input1 = input("enter PY name: ")
# SYS LDR
if input1 == "system":
  inpt = input("0:\\")
  if inpt == "stats":
    print(f"Statistics for USERNAME\REPL \n Times the launcher has been used: {RUNINT}")
# END SYS LDR
if input1 == "test":
  RUN = True
  import testo2k6l
print("")
print("")
print("")
print("")
print("------------------------------------------------------")
print("------------------------------------------------------")
print("Reached end of file. updating database")
if RUN == True:
  STLA = int(db["RUNINNIT"])
  TTL = STLA + 1
  db["RUNINNIT"] = TTL
print("------------------------------------------------------")
print("------------------------------------------------------")