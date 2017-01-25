import Tkinter
from Tkinter import *

top = Tk()
L1 = Label(text="Liczba 1")
L1.pack()

E1 = Entry(bd=5)
E1.pack()

L2 = Label(text="Liczba 2")
L2.pack()

E2 = Entry(bd=5)
E2.pack()

var = StringVar()
label = Label(top, textvariable=var, relief=RAISED)

def wyciagnij_wartosc():
    zmienna1 = int(E1.get())
    zmienna2 = int(E2.get())
    zmienna2 = zmienna2 + zmienna1
    var.set(str(zmienna2))
    label.pack()

def wyciagnij_wartosc1():
    zmienna1 = int(E1.get())
    zmienna2 = int(E2.get())
    zmienna2 = zmienna1 - zmienna2
    var.set(str(zmienna2))
    label.pack()

def wyciagnij_wartosc2():
    zmienna1 = int(E1.get())
    zmienna2 = int(E2.get())
    zmienna2 = zmienna1 * zmienna2
    var.set(str(zmienna2))
    label.pack()

def wyciagnij_wartosc3():
    zmienna1 = int(E1.get())
    zmienna2 = int(E2.get())
    zmienna2 = zmienna1 / zmienna2
    var.set(str(zmienna2))
    label.pack()

B = Tkinter.Button(top, text="Dodawanie", command=wyciagnij_wartosc)
B.pack()

B1 = Tkinter.Button(top, text="Odejmowanie", command=wyciagnij_wartosc1)
B1.pack()

B2 = Tkinter.Button(top, text="Mnozenie", command=wyciagnij_wartosc2)
B2.pack()

B3 = Tkinter.Button(top, text="Dzielenie", command=wyciagnij_wartosc3)
B3.pack()

top.mainloop()