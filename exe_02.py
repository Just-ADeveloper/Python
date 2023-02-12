class Ordenada:
    def __init__(self, palavras):
        self.palavras = palavras

    def sort_palavras(self):
        n = len(self.palavras)

        for i in range(n):
            indice_min = i
            for x in range(i+1, n):
                if self.palavras[x] < self.palavras[indice_min]:
                    indice_min = x
            self.palavras[i], self.palavras[indice_min] = self.palavras[indice_min], self.palavras[i]
        
        return self.palavras

palavras = ["zoro", "luffy", "usopp", "nami", "chopper", "brook", "sanji", "robin", "franky", "jinbei"]
Ordenada = Ordenada(palavras)
print(Ordenada.sort_palavras())
