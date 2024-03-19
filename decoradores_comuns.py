# Definição da classe MinhaClasse
class MinhaClasse:
    valor = 10  # Atributo de classe

    def __init__(self, nome) -> None:
        self.nome = nome  # Atributo da instância

    # Método de instância requer uma instância para ser chamado
    def metodo_instancia(self):
        return f"Método de instância chamado para {self.nome}"
  
    @classmethod
    def metodo_classe(cls):
        # Método de classe é chamado para a classe, pode acessar atributos de classe
        return f"Método de classe chamado para valor={cls.valor}"
  
    @staticmethod
    def metodo_estatico():
        # Método estático é independente de instâncias e classes
        return "Método estático chamado"
  
# Criando uma instância da classe MinhaClasse
obj = MinhaClasse(nome="Classe Exemplo")
print(obj.metodo_instancia())  # Chamando método de instância
print(MinhaClasse.valor)  # Acessando atributo de classe
print(MinhaClasse.metodo_classe())  # Chamando método de classe
print(MinhaClasse.metodo_estatico())  # Chamando método estático

# Definição da classe Carro
class Carro:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, configuracao):
        # Método de classe para criar uma instância de Carro a partir de uma string de configuração
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(ano))

# Criando um carro usando o método de classe
configuracao1 = "Toyota, Corolla,2022"
carro1 = Carro.criar_carro(configuracao1)
print(f"Marca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}")

# Definição da classe Matematica
class Matematica:
    @staticmethod
    def somar(a, b):
        # Método estático para somar dois números
        return a + b
  
# Usando o método estático somar da classe Matematica
print(Matematica.somar(a=10, b=15))
