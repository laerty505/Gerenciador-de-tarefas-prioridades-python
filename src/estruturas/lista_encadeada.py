class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def inserir_inicio(self, dado):
        novo_no = No(dado)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no

    def inserir_fim(self, dado):
        novo_no = No(dado)
        if self.cabeca is None:
            self.cabeca = novo_no
            return

        atual = self.cabeca
        while atual.proximo is not None:
            atual = atual.proximo
        atual.proximo = novo_no

    def remover(self, alvo):
        atual = self.cabeca
        anterior = None

        while atual is not None:
            if atual.dado == alvo:
                if anterior is None:
                    self.cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo

        return False

    def buscar(self, alvo):
        atual = self.cabeca
        while atual is not None:
            if atual.dado == alvo:
                return True
            atual = atual.proximo
        return False

    def exibir(self):
        elementos = []
        atual = self.cabeca
        while atual is not None:
            elementos.append(str(atual.dado))
            atual = atual.proximo
        return " -> ".join(elementos) if elementos else "Lista vazia"