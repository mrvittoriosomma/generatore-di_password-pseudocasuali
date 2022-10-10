import random

lower = "abcdefghijklmnopqrstuvwxyz"

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

numbers = "1234567890"

symbol = "!$%&()=?@#[]+-_."

all = lower + upper + numbers + symbol

nosymbol = lower + upper + numbers

verifica = 1

length = ""

while verifica == 1:
    length = input("Inserire la lunghezza desiderata: ")
    prova = length.isnumeric()
    if prova:
        verifica = 0
    else:
        verifica = 1

controllo = 1

scelta = ""

while controllo == 1:
    scelta = input("Con simboli (Y/N): ")
    if scelta == 'Y' or scelta == 'y' or scelta == 'N' or scelta == 'n':
        controllo = 0
    else:
        controllo = 1

if scelta == 'Y' or scelta == 'y':
    password = "".join(random.sample(all, int(length)))
    print("Password generata: " + password)

elif scelta == "N" or scelta == "n":
    password = "".join(random.sample(nosymbol, int(length)))
    print("Password generata: " + password)

