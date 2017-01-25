#tabliczka mnozenia i zapsywanie do pliku

f1 = open("zadanie2-domowe.txt","wb")
for x in range(1,11):
      print
      f1.write("\n")
      for y in range(1,11):
            print "%3i" % (x*y),
            f1.write(str("%4i" % (x*y)))
