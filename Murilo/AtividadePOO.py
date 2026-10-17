# 1 e 2. Criação da classe base Animal com Encapsulamento
class Animal:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        # Modificação da Q2: tornando a idade privada (__idade)
        if idade >= 0:
            self.__idade = idade
        else:
            self.__idade = 0
            print(f"Aviso: Idade negativa para {nome} inválida. Definida como 0.")

    # Métodos Getters e Setters para o atributo encapsulado
    def get_idade(self) -> int:
        return self.__idade

    def set_idade(self, nova_idade: int):
        if nova_idade >= 0:
            self.__idade = nova_idade
        else:
            print("Erro: A idade não pode ser negativa!")

    def exibir_dados(self):
        print(f"Nome: {self.nome} | Idade: {self.get_idade()} anos")

    def emitir_som(self):
        print("O animal está emitindo um som.")


# 3 e 4. Criação das subclasses (Herança) e Polimorfismo (Sobrescrita de Método)
class Cachorro(Animal):
    def emitir_som(self):
        print("Som: Au au")


class Gato(Animal):
    def emitir_som(self):
        print("Som: Miau")


class Passaro(Animal):
    def emitir_som(self):
        print("Som: Piado/Cantando (Curupaco!)")


# 5. Programa Principal - Criação dos objetos
cachorro = Cachorro("Rex", 3)
gato = Gato("Mimi", 2)
passaro = Passaro("Loro", 1)

# 6. Criação da lista e laço de repetição (for)
print("--- Listando Animais e Comportamentos ---")
animais = [cachorro, gato, passaro]

for animal in animais:
    animal.exibir_dados()
    animal.emitir_som()
    print("-" * 40)

#Questão 7

**a) Qual é a função da classe Animal no sistema? Como ela representa a abstração?
A classe `Animal` serve como um modelo conceitual e genérico (classe base). Ela representa a **Abstração** ao extrair e mapear apenas as propriedades (`nome`, `idade`) e comportamentos (`emitir_som`, `exibir_dados`) essenciais comuns a qualquer animal no escopo do software, ignorando detalhes complexos e desnecessários do mundo real.

**b) Por que utilizamos `__idade` em vez de deixar o atributo totalmente acessível?**
Utilizamos o prefixo duplo (`__idade`) para aplicar o **Encapsulamento** (usando o mecanismo de *name mangling* do Python). Isso protege o dado contra acessos ou modificações acidentais e diretas de fora da classe, garantindo que o estado interno do objeto só mude por regras validadas.

**c) Qual é a vantagem de utilizar herança nas classes Cachorro, Gato e Passaro?**
A maior vantagem da **Herança** é o **reuso de código**. Evita-se a duplicação desnecessária de lógica, pois as subclasses ganham automaticamente os atributos `nome`, `__idade` e o método `exibir_dados()` criados na classe `Animal`, facilitando manutenções futuras.

**d) Por que o método emitir_som() apresenta resultados diferentes para cada animal?**
Isso acontece por causa do **Polimorfismo**. Embora o método tenha exatamente a mesma assinatura (`emitir_som`), cada subclasse sobrescreveu a implementação padrão para responder à mensagem de uma forma específica correspondente à sua própria natureza.

**e) O que aconteceria se tentássemos cadastrar um animal com idade negativa? Como o programa poderia impedir isso também no momento da criação do objeto?**
No código original sem validação no construtor, o objeto aceitaria a idade inválida. Para impedir isso direto no momento da criação (instanciação), adicionamos uma condicional `if/else` dentro do método construtor `__init__` da classe `Animal` (conforme implementado no script acima), bloqueando ou corrigindo o valor antes de salvá-lo no atributo.
