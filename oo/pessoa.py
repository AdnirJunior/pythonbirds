class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola, meu nome é {(self.nome)}!'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mao'

class Mutante(Pessoa):
    olhos = 6



if __name__ == '__main__':
    renzo_jr = Homem(nome= 'Renzo Jr', idade= 15)
    renzo = Mutante(renzo_jr, nome= 'Renzo', idade= 47)

    print(renzo.nome)
    print(renzo.idade)
    print(Pessoa.cumprimentar(renzo_jr))
    renzo.olhos = 3
    for filho in renzo.filhos:
        print(filho.nome)
    renzo.sobrenome = 'Nucchitelli'
    print(renzo.sobrenome)
    print(renzo.__dict__)
    del renzo.filhos
    print(renzo.__dict__)
    print(Pessoa.olhos)
    print(renzo.olhos)
    print(Pessoa.metodo_estatico(), renzo.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), renzo.nome_e_atributos_de_classe())
    pessoa = Pessoa('anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(renzo_jr, Pessoa))
    print(isinstance(renzo_jr, Homem))
    print(Mutante.olhos)
    print(renzo.cumprimentar())
    print(renzo_jr.cumprimentar())


