# Definição de um decorador de função
def meu_decorator(func):
    def wrapper():
        print("Antes da função ser chamada")
        func()  # Chamada da função original
        print("Depois da função ser chamada")
    return wrapper

# Uso do decorador de função
@meu_decorator
def minha_funcao():
    print("Minha função foi chamada")

minha_funcao()

# Definição de um decorador de classe
class MeuDecoradorDeClasse:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self) -> any:
        print("Antes da função ser chamada (decorador de classe)")
        self.func()  # Chamada da função original
        print("Depois da função ser chamada (decorador de classe)")

# Uso do decorador de classe
@MeuDecoradorDeClasse
def segunda_funcao():
    print("Segunda função foi chamada")

segunda_funcao()
