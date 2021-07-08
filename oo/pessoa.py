class Pessoa:
    def __init__(self, nome = None, idade = 19):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Rodrigues')
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Bernardo'
    print(p.nome)
    print(p.idade)