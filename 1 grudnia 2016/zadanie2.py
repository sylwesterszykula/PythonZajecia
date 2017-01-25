from Tkinter import *
class LabelDemo(Frame):
    #dalsza instrukcja etykiet i przyciski
    def __init__(self):


        #tworzy trzy etykiety i dwa przysicki oraz pakuje je
        #tworzy obiekt ramka w ktorym umieszczam widgety
        #ramka jest upakowana w glownym oknie i ma tytul - Przyklad
        Frame.__init__(self)
        self.pack(expand = YES, fill = BOTH)
        self.master.title('Przyklad')

        #dwa przyciki QUIT i HEY
        #przycisniecie powoduje wywolanie metod quitl i say_hi
        #nazwy obiektow to button i hi_there
        self.button = Button(self, text="Quit", fg='red', command=self.quit1, width=16,height=1)
        self.hi_there = Button(self, text='Hey', command=self.say_hi, width=16,height=1)

        #3 pola etykiet = dwa tekstowe i ikone
        self.Label1 = Label(self,text='Etykieta tekstowa')
        self.Label2 = Label(self,text='Etykieta tekstowa z ikona')
        self.Label3 = Label(self, bitmap='warring')

        #pokowanie wszystkiego w ramke
        self.button.pack(side=BOTTOM)
        self.hi_there.pack(side=BOTTOM)
        self.Label1.pack()
        self.Label2.pack(side= LEFT)
        self.Label3.pack(side= LEFT)

        #metoda wywolywana poprzez nacisniece przycisku quit
    def quit1(self):
        print 'Konie'
        quit()

        #metoda wywolywana poprzez wcusniece przycisku hey
    def say_hi(self):
        print 'Elo'

#tworzenie okna LabelDemo i obsluga wszystkich zdarzen
def main():
    LabelDemo().mainloop()
    #jesli nazwa uruch programu to main wywalaj procedrue main
if __name__ == '__main__':
    main()