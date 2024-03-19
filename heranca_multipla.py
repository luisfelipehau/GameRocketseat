# Definição das classes
class Animal:
    def __init__(self, nome) -> None:
        # Método construtor da classe Animal. Recebe um parâmetro 'nome'.
        self.nome = nome

    def emitir_som(self):
        # Método que representa o som emitido pelo animal. Será sobrescrito nas subclasses.
        pass

class Mamifero(Animal):
    def amamentar(self):
        # Método específico para mamíferos que simula o ato de amamentar.
        return f"{self.nome} está amamentando."
  
class Ave(Animal):
    def voar(self):
        # Método específico para aves que simula o ato de voar.
        return f"{self.nome} está voando"
  
class Morcego(Mamifero, Ave):
    # Classe que herda de Mamifero e Ave simultaneamente (herança múltipla).
  
    def emitir_som(self):
        # Método sobrescrito que representa o som emitido pelos morcegos.
        return "Morcegos emitem sons ultrassônicos"
  
# Criando uma instância de Morcego
morcego = Morcego(nome="Batman")

# Acessando métodos da classe base `Animal`
print("Nome do morcego:", morcego.nome)
print("Som do morcego:", morcego.emitir_som())

# Acessando métodos das classes `Mamifero` e `Ave`
print("Morcego amamentando:", morcego.amamentar())
print("Morcego voando:", morcego.voar())
