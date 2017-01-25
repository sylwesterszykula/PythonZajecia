#podaje sciezke uzytkownik, wyswietlane sa inf o ilosci plikow, rozmiarze plikow
#ilosci folderow, rozmiaru tych folderow, oraz rozmiar calosciowy tego forlderu
#Ma to byc przeliczone na kilobajty i megabajty
from os import *


sciezka = raw_input('Podaj sciezke: ')

print listdir(sciezka)

for x in listdir('.'):
    if path.isdir(x) != True:
        print x, path.getsize(x)
        print x, path.getsize(x)*0.001
        print x, path.getsize(x)*0.000001


licznik = 0
for x in listdir('.'):
    if path.isdir(x) == True:
        licznik = licznik + 1

print licznik

licznik = 0
for root, dirs, files in walk('.', topdown=False):
    for name in files:
        print path.join(root, name)
        print path.getsize(name)
        print path.getsize(name)*0.001
        print path.getsize(name)*0.000001
        licznik = licznik + path.getsize(name)
    for name in dirs:
        print path.join(root, name)
        print path.getsize(name)
        print path.getsize(name)*0.001
        print path.getsize(name)*0.000001
        licznik = licznik + path.getsize(name)

print licznik
print licznik*0.001
print licznik*0.00001

