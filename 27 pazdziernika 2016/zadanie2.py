#klasy

class Napis:
    #klasa wyswietlajaca napis
    txt = 'Pierwsza klasa'
    def wyswietl(self):
        return 'Witaj'

#wywolanie obiekty klasy
napis = Napis()

#odwolanie do metody
print napis.wyswietl()

#odwolanie do atrybuty klasy
print napis.txt

#konkrety klasy
class Zespolona:
    def __init__(self,rzeczywista,urojona):
        self.r = rzeczywista;
        self.i = urojona

x = Zespolona(5.0,-3.2)
print x.r, x.i