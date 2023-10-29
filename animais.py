class animal():
    def __init__(self, nome, cor):
        self.nome=nome
        self.cor=cor

    def comer(self):
        print(f"o{self.nome} foi comer")

class gato(animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def miar(self):
        print(f"{self.nome} foi miando...")

class cachorro(animal):

    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def latir(self):
        print(f"{self.nome} foi latindo...")

class cavalo(animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def relinchar(self):
        print(f"{self.nome} foi relinchando...")

class croba(animal):
    
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def chiar(self):
        print(f"{self.nome} foi chiando...")

saka=gato("Sakamoto", "Frajola")
saka.miar()
su=cachorro("Suki", "tigrado")
su.latir()
xame=cavalo("Xamego", "Marrom")
xame.relinchar()
mik=croba("Sana", "Branca")
mik.chiar()