class Ordenada_cidades:
    def __init__(self, cidades):
        self.cidades = cidades

    def ordenar_cidades(self):
        n = len(self.cidades)

        for i in range(n):
            indice_min = i
            for j in range(i+1, n):
                if self.cidades[j] < self.cidades[indice_min]:
                    indice_min = j
            self.cidades[i], self.cidades[indice_min] = self.cidades[indice_min], self.cidades[i]
        
        return self.cidades

def main():
    cidades = []
    for i in range(5):
        cidade = input(f"Digite o nome da cidade {i+1}: ")
        cidades.append(cidade)
    
    ordena_cidades = Ordenada_cidades(cidades)
    cidades_ordenadas = ordena_cidades.ordenar_cidades()
    print("Cidades ordenadas:", cidades_ordenadas)

if __name__ == "__main__":
    main()
