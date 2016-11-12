#napisz skrypt ktory wykona nastepujace czynnosci
#utworzyc klase, podpunkty to osobne metody (najlepiej uniwersalne metody),

#a) utworzy liste o rozmiarach podanych przez uzytkownika
#b) uzupelni liste losowymi wartosciami z zakresu podanego przez uzytkownika
#c) wyswietli liste
#d) wyszuka wielokrotnosci liczby 2, 3, 5 i zapisze kazda do nowej listy
#e) wyszuka duplikaty z kazdej listy i utworzy z nich nowa liste
#f) zastapi duplikaty znakiem "X"
#g) usunie duplikaty z listy a)
#h) obliczy wartosc srednia i podniesie kazda wartosc do potegi 3
#i) zastapi wielokrotnosci liczby 2 litera A, 3 litera E, 5 litera L
#j) wyszuka liczby pierwsze i zastapi je litera Z
#k) wyszuka litery w liscie i utworzy z nich losowe napisy
import random
class ZadanieNaLekcji:
    list = []
    Lista = []
    def __init__(self, rozmiar_listy):
        self.rozmiar_listy = rozmiar_listy

    def tworzenie_Listy(self):
        ZadanieNaLekcji.Lista = [[0] * 1 for i in range(self.rozmiar_listy)]
        for i in range(self.rozmiar_listy):
            ZadanieNaLekcji.list.append(random.randint(1,100))

        #for i in ZadanieNaLekcji.list:
            #print i

    def szukanie_wielokrotnosci(self):
        flaga = True
        pom = 0
        for i in ZadanieNaLekcji.list:
            ZadanieNaLekcji.Lista[pom][0]=i
            ZadanieNaLekcji.Lista[pom].
            #for j in ZadanieNaLekcji.list:
            #    if i == j:
            #        ZadanieNaLekcji.Lista[pom]
            #    while flaga:
            pom = pom + 1

        for i in ZadanieNaLekcji.Lista:
            print i







znl1 = ZadanieNaLekcji(20)
znl1.tworzenie_Listy()
znl1.szukanie_wielokrotnosci()