#interfejsc graficzny do ciagu fibbo
import Tkinter
from Tkinter import *

wielkosc_tablicy = 61
tablica = dict()
tablica1 = dict()
for i in range(2,wielkosc_tablicy):
    tablica[i] = False

for i in range(2,wielkosc_tablicy):
    if tablica[i]:
        continue
    for j in xrange(i*2, wielkosc_tablicy, i):
        tablica[j] = True

zmienna = 0;
for i in tablica:
    if tablica[i] == False:
        tablica1[zmienna]=i
        zmienna = zmienna + 1
        #print i


root = Tk()
var = StringVar()
label = Label( root, textvariable=var, relief=RAISED)

def obliczCiag():
    var.set(tablica1)
    label.pack()

przycisk = Tkinter.Button(root, text="Oblicz ciag", command = obliczCiag)
przycisk.pack()
root.mainloop()