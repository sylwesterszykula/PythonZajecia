wielkosc_tablicy = input("Prosze podac gorny zakres przedzialu ")
wielkosc_tablicy = wielkosc_tablicy + 1
tablica = dict()

for i in range(2,wielkosc_tablicy):
    tablica[i] = False

for i in range(2,wielkosc_tablicy):
    if tablica[i]:
        continue
    for j in xrange(i*2, wielkosc_tablicy, i):
        tablica[j] = True

lista = []
for i in tablica:
    if tablica[i] == False:
        lista.append(i)
print lista

