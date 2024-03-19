# Exemplo de herança
print("\nExemplo de herança:")

class Animal:
    def __init__(self, nome) -> None:
        # Método construtor da classe Animal. Recebe um parâmetro 'nome'.
        self.nome = nome

    def andar(self):
        # Método que simula o ato de andar do animal.
        print(f"O animal {self.nome} andou")
        return

    def emitir_som(self):
        # Método que representa o som emitido pelo animal. Será sobrescrito nas subclasses.
        pass

# Subclasses Cachorro e Gato que herdam da classe Animal
class Cachorro(Animal):
    def emitir_som(self):
        # Método sobrescrito que representa o som de um cachorro.
        return "Au, au"
  
class Gato(Animal):
    def emitir_som(self):
        # Método sobrescrito que representa o som de um gato.
        return "Miau!"
  
dog = Cachorro(nome="Rex")
cat = Gato(nome="Felix")

# Exemplo de polimorfismo
print("\nExemplo de polimorfismo:")
animais = [dog, cat]

for animal in animais:
    # Iteração sobre a lista de animais, chamando o método emitir_som de cada um.
    print(f"{animal.nome} faz: {animal.emitir_som()}")

# Exemplo de encapsulamento
print("\nExemplo de encapsulamento:")
class ContaBancaria:
    def __init__(self, saldo) -> None:
        # Método construtor da classe ContaBancaria. Recebe um parâmetro 'saldo'.
        # O atributo __saldo é privado para encapsular o acesso direto a ele.
        self.__saldo = saldo  

    def depositar(self, valor):
        # Método para depositar dinheiro na conta bancária.
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        # Método para sacar dinheiro da conta bancária.
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
        # Método para consultar o saldo da conta bancária.
        return self.__saldo
    
conta = ContaBancaria(saldo=1000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor=500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor=-500)  # Tentativa de depositar um valor negativo
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.sacar(valor=2000)  # Tentativa de sacar um valor maior que o saldo
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

conta_do_zezinho = ContaBancaria(saldo=50)

# Exemplo de abstração
print("\nExemplo de abstração:")
from abc import ABC, abstractmethod

class Veiculo(ABC):
    # Classe abstrata que representa um veículo.

    @abstractmethod
    def ligar(self):
        # Método abstrato que define como um veículo deve ser ligado.
        pass

    @abstractmethod
    def desligar(self):
        # Método abstrato que define como um veículo deve ser desligado.
        pass

class Carro(Veiculo):
    # Classe que representa um carro, que é um tipo de veículo.

    def __init__(self) -> None:
        # Método construtor da classe Carro.
        pass

    def ligar(self):
        # Implementação do método abstrato ligar() para um carro.
        # Liga o carro usando a chave.
        return "Carro ligado usando a chave"
  
    def desligar(self):
        # Implementação do método abstrato desligar() para um carro.
        # Desliga o carro usando a chave.
        return "Carro desligado usando a chave"

carro_amarelo = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())
