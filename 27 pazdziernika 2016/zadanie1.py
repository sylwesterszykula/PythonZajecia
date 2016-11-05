#zbiory zmienne
A = set([1,2,3])
print A

#dodawanie u usuwanie elementow zbioru
A.discard(3)
print A

#dodawanie elementu 8
A.add(8)
print A

#zbiory niezmienne
B=frozenset([1,2,9,10])
print B

#klucze w slownikach
slownik = {B:9}
print slownik


#el innych zbiorow
C=set([5,4,9])
print C

#zbior pusty
D=set()
print D

#operacje na zbiorach


#liczba elementow
print len(A)
print len(B)

#sprawdzanie czy dany element jest elementem zbioru
print 5 in A
print 1 in A

#sprawdzenie czy dany obiekt nie jest elementem zbioru
print 5 not in A
print 1 not in A
print "LOLOL"

#sprawdzenie czy dany zbior jest podzbiorem innego zbioru
EE=set([1])
print set([1,2]) <= A
print set([1,2,3,4,5]) <= A
print set([3,4]) <= B

print EE.issubset(A)
print A.issubset(EE)

#laczenie zbiorow
E=A | B
print E

#czesc wspolna dwoch zbiorow
F=A & B
print F

#roznica dwoch zbiorow
print A-B
print B-A

#rownica symetryczna
G=A^B
print G
