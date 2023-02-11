class notaCalc:
    def __init__(self, notas):
        self.notas = notas

    def calcula_Media(self):
        total = 0
        for nota in self.notas:
            total += nota
        media = total / len(self.notas)
        return media

    def define_Status(self, media):
        if media < 4:
            return "Reprovado"
        elif media > 4 and media < 7:
            return "Reprovado com direito a exame final"
        elif media >= 7:
            return "Aprovado"

def main():
    notas = []
    for i in range(4):
        nota = float(input(f"Digite a nota {i+1}: "))
        while nota < 0 or nota > 10:
            print("nota inválida. Por favor, digite uma nota entre 0 e 10.")
            nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)
    
    nota_Calculada = notaCalc(notas)
    media = nota_Calculada.calcula_Media()
    status = nota_Calculada.define_Status(media)
    print("Média: {:.2f}".format(media))
    print("Status: {}".format(status))

if __name__ == "__main__":
    main()
