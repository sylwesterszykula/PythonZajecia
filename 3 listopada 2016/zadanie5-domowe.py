#skrypt ktory dziala jak ksiazka adresowa
#dane mozna wprowadzac, usunac, zmodyfikowac
#dane powinny byc wyswietlane w postaci tabeli
#przy operowaniu na danych mamy podac swoj pesel zeby miec uprawnienia
#imie, nazwisko, pesel, nr telefonu, email

class KsiazkaAdresowa:
    imie = ''
    nazwisko = ''
    pesel = 0
    nr_telefonu = 0
    email = ''

    def dodaj_nowego(self, imie, nazwisko, pesel, nr_telefonu, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.nr_telefonu = nr_telefonu
        self.email = email

koniec_petli_while = True
sterowanie_petli_while = 0

list_adresow = [KsiazkaAdresowa]

print 'Jezeli chcesz dodac uzytkownika, podaj 1'
print 'Jezeli chcesz usunac uzytkownika podaj 2'
print 'Jezeli chcesz zmodyfikowac dane podaj 3'
print 'Jezeli chcesz wyswietlic cala ksiazke podaj 4'
print 'Jezeli chcesz zakonczyc program podaj 5'

while koniec_petli_while:
    sterowanie_petli_while = input('Podaj liczbe: ')
    if sterowanie_petli_while == 1:
        print 'Wybrales 1 - dodawanie nowego uzytkownika'
        adres = KsiazkaAdresowa()
        adres.imie = raw_input('Podaj imie: ')
        adres.nazwisko = raw_input('Podaj nazwisko: ')
        adres.pesel = input('Podaj pesel: ')
        adres.nr_telefonu = input('Podaj numer telefonu: ')
        adres.email = raw_input('Podaj adres email: ')
        list_adresow.append(adres)
        print 'Pomyslnie dodano nowy adres do ksiazki'

    if sterowanie_petli_while == 2:
        print 'Wybrales 2 - usuwanie uzytkownika'
        autoryzacja_peselu_usuwanie = input('Ze wzgledu bezpieczenstwa podaj swoj pesel: ')
        licznik = 0
        for i in list_adresow:
            if i.pesel == autoryzacja_peselu_usuwanie:
                print 'Witamy uzytkownika', i.imie
                del list_adresow[licznik]
                print 'Uzytkownik zostal pomyslnie usuniety'
                break
            licznik = licznik + 1

    if sterowanie_petli_while == 3:
        print 'Wybrales 3 - modyfikacja danych'
        autoryzacja_peselu_modyfikowanie = input('Ze wzgledu bezpieczenstwa podaj swoj pesel: ')
        licznik = 0
        for i in list_adresow:
            if i.pesel == autoryzacja_peselu_modyfikowanie:
                print 'Witamy uzytkownika', i.imie

                sterowanie_petli_while_modyfikacje = 0
                koniec_petli_while_modyfikacje = True

                print 'Jezeli chcesz zmodyfikowac imie podaj 1'
                print 'Jezeli chcesz zmodyfikowac nazwisko podaj 2'
                print 'Jezeli chcesz zmodyfikowac pesel podaj 3'
                print 'Jezeli chcesz zmodyfikowac numer telefonu podaj 4'
                print 'Jezeli chcesz zmodyfikowac adres email podaj 5'
                print 'Jezeli zakonczyles modyfikacje podaj 6'

                while koniec_petli_while:
                    sterowanie_petli_while_modyfikacje = input('Podaj liczbe: ')
                    if sterowanie_petli_while_modyfikacje == 1:
                        print 'Wybrales 1'
                        i.imie = raw_input('Podaj nowe imie: ')
                        print 'Nowe imie to: ', i.imie
                    if sterowanie_petli_while_modyfikacje == 2:
                        print 'Wybrales 2'
                        i.nazwisko = raw_input('Podaj nowe nazwisko: ')
                        print  'Nowe nazwisko to: ', i.nazwisko
                    if sterowanie_petli_while_modyfikacje == 3:
                        print 'Wybrales 3'
                        i.pesel = input('Podaj nowy pesel: ')
                        print 'Nowy pesel to: ', i.pesel
                    if sterowanie_petli_while_modyfikacje == 4:
                        print  'Wybrales 4'
                        i.nr_telefonu = input('Podaj nowy numer telefonu: ')
                        print 'Nowy numer telefonu to: ', i.nr_telefonu
                    if sterowanie_petli_while_modyfikacje == 5:
                        print 'Wybrales 5'
                        i.email = raw_input('Podaj nowy adres email: ')
                        print 'Nowy adres email: ', i.email
                    if sterowanie_petli_while_modyfikacje == 6:
                        print 'Wybrales 6, przejedziesz teraz do glownego menu'
                        break
    if sterowanie_petli_while == 4:
        print 'Wybrales 4 - wyswietlanie wszystkich uzytkownikow'

        for i in list_adresow:
            if i.imie != '':
                print '{0:10}  {1:10}  {2:10d}  {3:10d}  {4:10}'.format(i.imie, i.nazwisko, i.pesel, i.nr_telefonu, i.email)

    if sterowanie_petli_while == 5:
        print 'Wybrales 5, Czesc!'
        koniec_petli_while = False
