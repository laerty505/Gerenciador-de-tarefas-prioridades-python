class Pilha:
    def __init__(self):
        self.itens = []  # Lista interna para armazenar os elementos

    def esta_vazia(self):
        return len(self.itens) == 0

    def empilhar(self, elemento):
        self.itens.append(elemento)  # Adiciona ao topo

    def desempilhar(self):
        if self.esta_vazia():
            raise IndexError("A pilha está vazia. Não é possível desempilhar.")
        return self.itens.pop()  # Remove e retorna o topo

    def topo(self):
        if self.esta_vazia():
            raise IndexError("A pilha está vazia.")
        return self.itens[-1]  # Retorna o elemento do topo sem remover

    def tamanho(self):
        return len(self.itens)

    def __str__(self):
        return str(self.itens)