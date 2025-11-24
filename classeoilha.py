# Classe Pilha
class Pilha:
    def __init__(self):
        self.__pilha = []

    def inserir(self,item):
        # Adiciona no topo
        self.__pilha.append(item)

    def remover(self):
        # Remove do topo (último que entrou)
        return self.__pilha.pop()

    def __str__(self):
        return str(self.__pilha)


# Testando a pilha
pilha_estudante = Pilha()

pilha_estudante.inserir("estudante 1")
pilha_estudante.inserir("estudante 2")
pilha_estudante.inserir("estudante 3")

print(f"Pilha atual: {pilha_estudante}")

# (LIFO) o último a entrar sai primeiro:
atendido = pilha_estudante.remover()
print(f"Estudante atendido (do topo): {atendido}")

print(f"Pilha depois de atender: {pilha_estudante}")
