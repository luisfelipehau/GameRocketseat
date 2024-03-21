import random


class Personagem:
    """Classe base para representar um personagem do jogo."""

    def __init__(self, nome, vida, nivel):
        """Inicializa um personagem com nome, vida e nível."""
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        """Retorna o nome do personagem."""
        return self.__nome

    def get_vida(self):
        """Retorna a vida atual do personagem."""
        return self.__vida

    def get_nivel(self):
        """Retorna o nível do personagem."""
        return self.__nivel

    def exibir_detalhes(self):
        """Exibe os detalhes do personagem, incluindo nome, vida e nível."""
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"

    def receber_ataque(self, dano):
        """
        Aplica o dano recebido ao personagem, subtraindo-o da vida.
        Se a vida ficar abaixo de 0, é ajustada para 0.
        """
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0

    def atacar(self, alvo):
        """
        Realiza um ataque ao alvo, causando um dano aleatório com base no nível do atacante.
        """
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")


class Heroi(Personagem):
    """Classe para representar um herói, derivada da classe Personagem."""

    def __init__(self, nome, vida, nivel, habilidade):
        """Inicializa um herói com nome, vida, nível e habilidade especial."""
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        """Retorna a habilidade especial do herói."""
        return self.__habilidade

    def exibir_detalhes(self):
        """Exibe os detalhes do herói, incluindo a habilidade especial."""
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"

    def ataque_especial(self, alvo):
        """
        Realiza um ataque especial ao alvo, causando um dano aumentado com base no nível do herói.
        """
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8)
        alvo.receber_ataque(dano)
        print(
            f"{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano!"
        )


class Inimigo(Personagem):
    """Classe para representar um inimigo, derivada da classe Personagem."""

    def __init__(self, nome, vida, nivel, tipo):
        """Inicializa um inimigo com nome, vida, nível e tipo."""
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        """Retorna o tipo do inimigo."""
        return self.__tipo

    def exibir_detalhes(self):
        """Exibe os detalhes do inimigo, incluindo o tipo."""
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}\n"


class Jogo:
    """Classe orquestradora do jogo."""

    def __init__(self) -> None:
        """Inicializa o jogo com um herói e um inimigo."""
        self.heroi = Heroi(nome="Herói", vida=100, nivel=5, habilidade="Super Força")
        self.inimigo = Inimigo(nome="Morcego", vida=50, nivel=3, tipo="Voador")

    def iniciar_batalha(self):
        """Faz a gestão da batalha em turnos."""
        print("Iniciando batalha!")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos Personagens:")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Pressione Enter para atacar...")
            escolha = input("Escolha (1 - Ataque Normal, 2 - Ataque Especial): ")

            if escolha == "1":
                self.heroi.atacar(self.inimigo)
            elif escolha == "2":
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("Escolha inválida. Escolha novamente.")

            if self.inimigo.get_vida() > 0:
                # Inimigo ataca o heroi
                self.inimigo.atacar(self.heroi)

        if self.heroi.get_vida() > 0:
            print("\nParabéns você venceu a batalha!")
        else:
            print("\nVocê foi derrotado!")


# Criar instância do jogo e iniciar batalha
jogo = Jogo()
jogo.iniciar_batalha()
