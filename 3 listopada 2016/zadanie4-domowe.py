#napisac skrypt ktory bedzie dziala jak gra w zgadywanie liczby
#liczby losowana z zakresu podanego przez uzytkownika
#wybra ilos prob ktora uzytkonik moze zgadywac
#procez zgadywana

import random
liczbapodanaprzezuzytkownika = 0

print 'Podaj zakres z jakiego beda losowane liczby: a, b'
a = input('Podaj a: ')
b = input('Podaj b: ')

l = range(a,b)
wylosowanaliczba = random.choice(l)


ilosprobuzytkonika = 0
ilosprobuzytkonika = input('Ile razy chcesz losowac: ')

for i in range(0,ilosprobuzytkonika):
    liczbapodanaprzezuzytkownika = input()
    if wylosowanaliczba == liczbapodanaprzezuzytkownika:
        print 'Gratulacje trafile'
        break
    elif wylosowanaliczba < liczbapodanaprzezuzytkownika:
        print 'Podajesz za duze liczby'
    else:
        print 'Podajesz za male liczby'
print 'Wylosowana liczba byla liczba: ', wylosowanaliczba