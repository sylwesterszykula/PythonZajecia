#napisz skrypt ktory wylicza najwiekszy wspolny dzielnik i najwieksza wspolna wielokrotnosc
a = 28
b = 24
def nwd(a, b):
    while b:
        a, b = b, a%b
    return a

a = nwd(a,b);
print a

c = 20
d = 30

e = nwd(c,d)
e = c/e
d = d*e
print d