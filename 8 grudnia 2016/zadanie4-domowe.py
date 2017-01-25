#konwertowanie typow liczbowych, zamienianie na system 8 i 2 z 10

import Tkinter
from Tkinter import *
def wyswietlaniePoKonwersji(zmienna):
    varGotowaLiczba.set(zmienna)
    label.pack()
def dokonajZamiany():
    if varNaJakiSystem.get() == 1:
        zmienna = int(E1.get())
        zmienna = oct(zmienna)
        wyswietlaniePoKonwersji(zmienna)
    if varNaJakiSystem.get() == 2:
        zmienna = int(E1.get())
        zmienna = bin(zmienna)
        wyswietlaniePoKonwersji(zmienna)


top = Tk()
L1 = Label(text="Podaj liczbe w systemie 10")
L1.pack()

E1 = Entry(bd=5)
E1.pack()

varGotowaLiczba = IntVar()
label = Label(top, textvariable=varGotowaLiczba, relief=RAISED)

varNaJakiSystem = IntVar()
for text, value in [('Konwersja liczby na system 8', 1), ('Konwersja liczby na system 2', 2)]:
    Radiobutton(top, text=text, value=value, variable=varNaJakiSystem, command=dokonajZamiany).pack(anchor=W)














top.mainloop()