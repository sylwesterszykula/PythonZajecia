from Tkinter import *
from tkMessageBox import *

class EntryDemo( Frame ):
    #demonstruje cztery pola tekstowe
    def __init__(self):
        #tworzy, pakuje i binduje zdarzenia do pol tekstowych
        Frame.__init__( self )
        self.pack( expand=YES, fill=BOTH)
        self.master.title("Testowanie pol tekstowych")
        self.master.geometry("325x100")

        self.frame1 = Frame(self)
        self.frame1.pack(pady=5)

        self.text1 = Entry(self.frame1, name="Tekst 1")
        self.text1.bind("<Return>", self.showContents)
        self.text1.pack(side=LEFT, padx=5)

        self.text2 = Entry(self.frame1, name="Tekst 2")
        self.text2.insert(INSERT, "Wpisz tekst tutaj")
        self.text2.bind("<Return>", self.showContents)
        self.text2.pack(side=LEFT, padx=5)


        self.frame2 = Frame(self)
        self.frame2.pack(pady=5)

        self.text3 = Entry(self.frame2, name="Tekst 3")
        self.text3.insert(INSERT, "Pole nieedytowalne")
        self.text3.config(state=DISABLED)
        self.text3.bind("<Return>", self.showContents)
        self.text3.pack(side=LEFT, padx=5)

        #tekst w polu tekstowym4 pojawia sie zagwiazdkowany
        self.text4 = Entry(self.frame2, name="Tekst 4", show="*")
        self.text4.insert(INSERT, "Tekst ukryty")
        self.text4.bind("<Return>", self.showContents)
        self.text4.pack(side=LEFT, padx=5)

    def showContents(self, event):
        #wyswietl zawartosc pola
        #wyswietl naze pola tekstowego generujacego zdarzenia
        theName = event.widget.winfo_name()
        #podstaw zawartosc tego pola do zmniennej theContents
        theContents = event.widget.get()
        #po wypelnieniu pola tekstowego i wcisnieciu enter zwartosc tego pola znajduje sie w theContents a tu dla fun drukujemy je w osobnym oknie modlulu MessageBoc
        showinfo("Komunikat", theName + ": " + theContents)
def main():
    EntryDemo().mainloop()
if __name__ == "__main__":
    main()
