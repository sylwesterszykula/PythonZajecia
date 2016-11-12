#do zadanie7-praca domowa dodaj zeby wczytywalo od uzytkownika oraz wyswietlanie ma
#byc w postaci tabeli jak w zadaniu zadanie5pracadomowa

#wytworniki list

l=range(1,21,2)
print l

#postac prosta


#podwojenie wartosci
print (2*x for x in l)


#para (x, kwadrat x)
print [(x,x*x) for x in range(1,5)]

#tabela kodowa ASCII
print [(x, ord(x)) for x in "ABCDF"]

#lista zawierajaca 10 pustych list
print [ [] for x in range(10)]

#postac prosta warunkowa
#liczby wieksze od 10
print [x for x in l if x>10]

#liczby podzielne przez 3 lub 5
print [x for x in range(1,20) if not (x%3) or not (x%5)]

#tabela kodowa ASCII dla samoglosek
print [(x, ord(x)) for x in "ABCDEF" if x in "AEIOUY"]

#postac rozszerzona
#pary kazdy element z kazdym
print [(x,y) for x in range(1,5) for y in range(4,0,-1)]


#roznica miedzy wrtosciua z pierwszej i drugiej listy
print [x-y for x in range(1,5) for y in range(4,0,-1)]

#sklejanie napisu z wartosci pochodzacych z trzech list
print [`x`+y+`z` for x in [1,2]
    for y in ['A','B']
    for z in [0,3]]

#postac rozszerzona z jendym warunkiem
#para kazdy element z kazdym tylko jezeli pierwszy element jest mniejszy od drugiego
print [(x,y) for x in range(1,5) for y in range(6,3,-1) if x<y]

#para kazdy element z kazdym tylko jezeli suma elementow jest mniejsza od 7
print [(x,y) for x in range(1,5) for y in range(6,3,-1) if x+y<7]

#PARA KAZDY ELEMENT Z KAzdym pod warunkiemze pierwszy element jest parzysty a drugi jest nie parzysty
print [(x,y) for x in range(1,5)
                for y in range(7,2,-1)
                    if not (x%2) or (y%2)]

#postac rozszerzona z wieloma warunkami
#para kazdy element z kazdym pod warunkiem ze pierwszy element jest parzysty a drugi jest nie parzysty
print [(x,y) for x in range(1,5) if not (x%2) for y in range(6,2,-1) if y%2]
