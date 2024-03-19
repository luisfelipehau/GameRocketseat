# Definindo a classe Pessoa
class Pessoa:
    def __init__(self, nome, idade) -> None:
        # O método __init__ é o construtor da classe, utilizado para inicializar seus atributos.
        # self é uma referência à instância da classe (o objeto criado a partir dela).
        # Neste caso, nome e idade são atributos que pertencem a cada instância de Pessoa.
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        # Método saudacao() retorna uma saudação com o nome e idade da pessoa.
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

# Criando objetos (instâncias) da classe Pessoa
pessoa1 = Pessoa("Alice", 30)
# Criamos uma instância chamada pessoa1 com nome "Alice" e idade 30.
mensagem = pessoa1.saudacao()  # Chamando o método saudacao() da instância pessoa1.
print(mensagem)  # Imprimindo a mensagem de saudação.

pessoa2 = Pessoa(nome="Rodrigo", idade=32)
# Criamos outra instância chamada pessoa2 com nome "Rodrigo" e idade 32.
mensagem = pessoa2.saudacao()  # Chamando o método saudacao() da instância pessoa2.
print(mensagem)  # Imprimindo a mensagem de saudação.
