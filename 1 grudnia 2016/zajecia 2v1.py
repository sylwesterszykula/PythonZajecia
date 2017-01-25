"""Etykiety i przyciski"""
from Tkinter import *
class LabelDemo( Frame ):
    """Dalsza ilustracja etykiet i przyciski"""
    def __init__( self ):
        """Tworzy trzy etykiety i dwa przyciski oraz pakuje je"""
        #tworzy obiekt ramka w ktorym umieszczamy widgety
        #ramka jest upakowana w glownym oknie i ma tytul - Przyklad
        Frame.__init__(self)
        self.pack(expand = YES, fill = BOTH)
        self.master.title("Przyklad")

        #Tworzymy dwa przyciski o nazwach QUIT i Hej ktorych wcisniecie
        #Powoduje wywolanie metod quit1 i say_hi odpowiednio
        #Nazwy obiektow to button i hi_there
        self.button = Button(self, text="Quit", fg="red",command=self.quit1, width=16, height=1)
        self.hi_there = Button(self, text="Hej", command = self.say_hi, width=16, height = 1)
        #Tworzymy trzy pola etykiet - dwa tekstowe i ikone
        self.Label1 = Label(self, text="Etykieta tekstowa")
        self.Label2 = Label(self, text="Etykieta tekstowa z ikona")
        self.Label3 = Label(self, bitmap="warning")
        #Teraz pakujemy wszystko w ramce
        self.button.pack(side=BOTTOM)
        self.hi_there.pack(side=BOTTOM)
        self.Label1.pack()
        self.Label2.pack(side= LEFT)
        self.Label3.pack(side= LEFT)

    #Metoda wywolywana przez wcisniecie przycisku QUIT
    def quit1(self):
            print "Koniec"
            quit()
    #Metoda wywolywana przez wcisniecie Hej
    def say_hi(self):
        print "Hej - Witojcie!"

# (A) Program glowny - utworzenie okna LabelDemo i obsluga wszystkich zdarzen
def main():
    LabelDemo().mainloop()
#Jesli nazwa uruchamianego programu to __main__ wywolaj procedure main().
if __name__ == "__main__":
   main()



