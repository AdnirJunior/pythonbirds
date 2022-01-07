class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola {id(self)}'


if __name__ == '__main__':
    renzo_jr = Pessoa(nome= 'Renzo Jr', idade= 15)
    renzo = Pessoa(renzo_jr, nome= 'Renzo', idade= 47)

    print(renzo.nome)
    print(renzo.idade)
    for filho in renzo.filhos:
        print(filho.nome)


