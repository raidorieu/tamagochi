class tamagochi:
    def __init__(self, n, i, p):
        self.nome=n
        self.idade=i
        self.peso=p
        self.comendo=False
        self.andando=False
        self.dormindo=False
    def comer(self, comida):
        if self.comendo== False:
            self.comendo= True
            print(f"{self.nome} começou a comer {comida}")
        elif self.andando==True:
            print(f"{self.nome} não pode comer, tá andando")
        elif self.dormindo==True:
            print(f"{self.nome} não pode comer, tá dormindo")
        else:
            print(f"{self.nome} tá comendo {comida}")


    def parardecomer(self):
        if self. comendo==True:
            self.comendo=False
            print("Parou de comer")
        else:
            print(f"{self.nome} não está comendo")

    def andar(self, aonde):
        if self.andando== False:
            self.andando= True
            print(f"{self.nome} começou a andar em {aonde}")
        elif self.comendo== True:
            print(f"{self.nome} não pode andar, tá comendo")
        elif self.dormindo== True:
            print(f"{self.nome}, não pode andar, tá comendo")
        else:
            print(f"{self.nome} já está andando em {aonde}")

    def parardeandar(self):
        if self.andando==True:
            self.andando=False
            print(f"{self.nome} parou de andar")
        else:
            print(f"{self.nome} não está andando")

    def dormir(self, horas):
        if self.dormindo== False:
            self.dormindo= True
            print(f"{self.nome} foi dormir às {horas} horas")
        elif self.comendo== True:
              print(f"{self.nome} não pode dormir, tá comendo")
        elif self.andando==True:
            print(f"{self.nome} não pode dormir, tá andando")
        else:
            print(f"{self.nome} já está dormindo")




