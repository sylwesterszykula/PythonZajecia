l = [1,2,'element',3.14] #lista
print l

k=(1,2,'element',3.14) #tupla...
print k

print l[1]

print k[1]

print l[1:3]

print l[1:len(l)]

print k[:-2]

print 1 in l

l[0] = 3
print l

# k[0]=3 blad kompilacji, nie mozna przepisac wartosci w tupli
# print k

l[1:3]=['a', 'b']
print l