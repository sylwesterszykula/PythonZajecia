#ZadanieNaLekcji.ListaLista = [[0] * 1 for i in range(self.rozmiar_listy)]

Lista = [[0]*1 for i in range(10)]

Lista[0][0] = 10
Lista[0].append(1)
print Lista[0]