class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome = None, idade = 19):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'


class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    Bernardo = Mutante(nome = 'Bernardo')
    Antonio = Homem(Bernardo, nome = 'Antonio')
    print(id(Bernardo))
    print(Bernardo.cumprimentar())
    print(Antonio.nome)
    for filho in Antonio.filhos:
        print(filho.nome)
    Antonio.sobrenome = 'Rodrigues'
    del Antonio.filhos
    Antonio.olhos = 1
    del Antonio.olhos
    print(Antonio.__dict__)
    print(Bernardo.__dict__)
    print(Antonio.olhos, Bernardo.olhos)
    print(id(Pessoa.olhos), id(Bernardo.olhos), id(Antonio.olhos))
    print(Pessoa.metodo_estatico(), Antonio.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), Antonio.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa), isinstance(pessoa, Homem))
    print(isinstance(Bernardo, Pessoa), isinstance(Bernardo, Homem))
    print(Bernardo.olhos)
    print(Antonio.cumprimentar())
    print(Bernardo.cumprimentar())