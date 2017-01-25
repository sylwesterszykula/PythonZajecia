#utoworzenie i otwarcie do zapisu pliku "plik1.txt"

f1 = open("plik1.txt","wb")

# 3 podstawowe atrybuty obiektow plikowych

#name - nazwa pliku

print f1.name

#mode = okresla tryb w jaki otwarto plik

print f1.mode

#closed - okresla czy plik jest zamkniety

print f1.closed


#metody do obslugi plikow

#write - zapisuje do pliku napis
f1.write("Pierwszy plik")

#flash - zapisuje dane z bufora do pliku
f1.flush()

#\n - nowa linia pliku

f1.write("\n nowa linia")

#close - zapisuje dane z bufora pliku i zamyka plik

f1.close()

#otwarcie pliku do modyfikacji

f1 = open("plik1.txt", "r+b")

#read - odczytuje z pliku napis

print f1.read()

#tell - podaje aktualna pozycje w pliku
print f1.tell()

#seek - ustawia pozycje w pliku na podana
f1.seek(0)

#nadpisanie zawartosci pliku
f1.write("Nowy poczatek")

#przesuniecie na wzgledna pozycje pliku (od aktualnej pozycji)
f1.seek(-13,1)

#wczytanie fragmentu zawartosci pliku o okreslonej dlugosci
print f1.read(14)

#writelines - zapisuje do pliku sekwencje napisow(bez dodawania automatycznie separatorow)
f1.writelines(["\n3 linia", "\n4 linia", "\n5 linia"])

#read linies - wczytuje z pliku sekwencje napisow
f1.seek(0)
print f1.readline()

#truncate - skraca plik na podane pozycji
f1.truncate(30)
f1.seek(0)
print f1.read()

#isatty - zwraca true jezeli plik jest dolaczony do urzadzenia terminalnego
print f1.isatty()

#przyklad strumienie sys.stdout i sys.stdin
import sys
print sys.stdout.isatty()

#przyklad przekierowania wewnatrz programu
import sys
ekran = sys.stdout
sys.stdout
sys.stdout = open("wyjscie.txt","w")
print "Jestem tutaj"
print "Gdzie poszedles?"
sys.stdout = ekran
print open("wyjscie.txt","r").read()