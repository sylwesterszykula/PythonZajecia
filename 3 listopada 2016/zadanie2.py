class Adres:
    pass
adr1 = Adres() #utworzenie rekordu
adr1.ulica = 'Stonogi'
adr1.nr = 23
adr1.kod = '22-440'
adr1.miasto = 'Dno'

print adr1.ulica
print adr1.__dict__

