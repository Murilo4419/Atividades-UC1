class Conta:
    def __init__(self, saldo):
        self.saldo = saldo

    def sacar(self, valor):    
        # Verificar se o valor é positivo E se é menor ou igual ao saldo
        if valor > 0 and valor <= self.saldo:
           self.saldo -= valor
           print("Saque realizado!")
        else: 
           print("Saque inválido!")    


# Criando a conta com 100 de saldo
conta_do_cliente = Conta(100)

# Testando um saque válido
conta_do_cliente.sacar(30)
# Vai imprimir: "Saque realizado!"

# Testando um saque inválido  (maior que o saldo)
conta_do_cliente.sacar(200)
# Vai imprimir saque: "Saque inválido!"

# Mostrando o saldo final
print("O saldo final é:", conta_do_cliente.saldo)

class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def mostrar_dados(self):
        print("Produto:", self.nome)
        print("Preço: R$", self.preco)
        print("Estoque:", self.estoque)

    def vender(self, quantidade):
        if quantidade > 0 and quantidade <= self.estoque:
            self.estoque -= quantidade
            print("Venda realizada!")

        else:
            print("Venda inválida")     

produto1 = Produto("Mouse", 50, 10)
produto2 = Produto("Teclado", 120, 5)

produto1.mostrar_dados()
produto1.vender(3)
produto1.mostrar_dados()

produto2.mostrar_dados()
produto2.vender(2)
produto2.mostrar_dados()

class Cidade:
    def __init__(self, cidade, temperatura, unidade):
        self.cidade = cidade
        self.temperatura = temperatura
        self.unidade = unidade

    def atualizar_temperatura(self, nova_temp):
        self.temperatura = nova_temp

        if self.temperatura < -60 and self.temperatura > 60:
           print("ALERTA:")

    def classificar_clima(self):
        if self.temperatura < 20:
            return "Frio"
        elif self.temperatura <= 30:
            return "Agradável"
        else:
            return "Quente"

    def relatorio(self):
        print("Estação Meteorológica")
        print("Cidade: ", self.cidade)
        print("Temperatura: ", self.temperatura and self.unidade)
        print("Classificação do clima: ", self.classificar_clima()) 

cidade1 = Cidade("Petrolina", 35, "C°")   

cidade1.atualizar_temperatura(40)
cidade1.classificar_clima()
cidade1.atualizar_temperatura(40)
