class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 19):
        self.idade = idade
        self.nome = nome
        self.filhos =list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    Bernardo = Pessoa(nome = 'Bernardo')
    Antonio = Pessoa(Bernardo, nome = 'Antonio')
    print(id(Bernardo))
    print(Bernardo.cumprimentar())
    print(Antonio.nome)
    for filho in Antonio.filhos:
        print(filho.nome)
    Antonio.sobrenome = 'Rodrigues'
    del Antonio.filhos
    print(Antonio.__dict__)
    print(Bernardo.__dict__)
