from Tkinter import*
from tkMessageBox import *

class EntryDemo(Frame):
    "Demonstruje cztery pola tekstowe"
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand = YES, fill = BOTH)
        self.master.title("testowanie pol tekstowych")
        self.master.geometry("325x100")

        self.frame1 = Frame( self )
        self.frame1.pack(pady = 5)

        self.text1 = Entry( self.frame1, name = "text 1")
        self.text1.bind("<Return>", self.showContents)
        self.text1.pack(side = LEFT, padx=5)

        self.text2 = Entry(self.frame1, name="text 2")
        self.text2.insert(INSERT, "Wpisz tekst tutaj")
        self.text2.bind("<Return>", self.showContents)
        self.text2.pack(side=LEFT, padx=5)

        self.frame2 = Frame(self)
        self.frame2.pack(pady=5)

        self.text3 = Entry(self.frame2, name="text 3")
        self.text3.insert(INSERT, "Pole nieedytowalne")
        self.text3.config(state = DISABLED)
        self.text3.bind("<Return>", self.showContents)
        self.text3.pack(side=LEFT, padx=5)

        #text in polu text4 pojawia sie jako *

        self.text4 = Entry(self.frame2, name="text 4", show = "*")
        self.text4.insert(INSERT, "Tekst ukryty")
        self.text4.config(state=DISABLED)
        self.text4.bind("<Return>", self.showContents)
        self.text4.pack(side=LEFT, padx=5)

    def showContents(self, event):
        "wyswietla zawartosc pola"
        #wyswietl zawartosc pola tekstowego generujacego zdarzenie
        theName = event.widget.winfo_name()
        #podstaw zawartosc tego pola do zmiennej theContents
        theContents = event.widget.get()
        #Po wypelnienieu pola tekstowego i wcisnieciu ENTER
        #Zawartosc tego pola znajduje sie w theContents
        #dla celow szkoleniowych drukujemy je w osobnym oknie modulu messageBox
        showinfo("Komunikat", theName + ": "+theContents)
def main():
    EntryDemo().mainloop()
if __name__ == "__main__":
    main()