class Cidade:
    def __init__(self, cidade, temperatura, unidade):
        self.cidade = cidade
        self.temperatura = temperatura
        self.unidade = unidade

    def mostrar_dados(self):
        print("Cidade: ", self.cidade)
        print("Temperatura: ", self.temperatura)
        print("Unidade: ", self.unidade)


    def atualizar_temperatura(self, nova_temp):
        self.temperatura = nova_temp

        if self.temperatura < -60 or self.temperatura > 60:
           print("ALERTA: Clima extremo")

    def classificar_clima(self):
        if self.temperatura < 20:
            print("Frio")
        elif self.temperatura <= 30:
            print("Agradável")
        else:
            print("Quente")

    def relatorio(self):
        print("Estação Meteorológica")
        print("Cidade: ", self.cidade)
        print("Temperatura: ", self.temperatura)
        print("Unidade: Celsius")
        self.classificar_clima

cidade1 = Cidade("Petrolina", 15, "Celsius")   

cidade1.mostrar_dados()
cidade1.classificar_clima()
cidade1.atualizar_temperatura(40)
cidade1.mostrar_dados()
cidade1.classificar_clima()
cidade1.relatorio()