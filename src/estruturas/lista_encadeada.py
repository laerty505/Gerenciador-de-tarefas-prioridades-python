class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
        self._tamanho = 0

    def inserir_inicio(self, dado):
        novo_no = No(dado)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no
        self._tamanho += 1

    def inserir_fim(self, dado):
        novo_no = No(dado)
        if self.cabeca is None:
            self.cabeca = novo_no
            self._tamanho += 1
            return

        atual = self.cabeca
        while atual.proximo is not None:
            atual = atual.proximo
        atual.proximo = novo_no
        self._tamanho += 1

    def tamanho(self):
        return self._tamanho

    def obter(self, indice):
        atual = self.cabeca
        for _ in range(indice):
            atual = atual.proximo
        return atual.dado

    def definir(self, indice, dado):
        atual = self.cabeca
        for _ in range(indice):
            atual = atual.proximo
        atual.dado = dado

    def remover_indice(self, indice):
        atual = self.cabeca
        anterior = None
        for _ in range(indice):
            anterior, atual = atual, atual.proximo
        if anterior is None:
            self.cabeca = atual.proximo
        else:
            anterior.proximo = atual.proximo
        self._tamanho -= 1
        return atual.dado

    def remover_identidade(self, alvo):
        atual = self.cabeca
        anterior = None
        while atual is not None:
            if atual.dado is alvo:
                if anterior is None:
                    self.cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self._tamanho -= 1
                return True
            anterior, atual = atual, atual.proximo
        return False

    def remover(self, alvo):
        atual = self.cabeca
        anterior = None

        while atual is not None:
            if atual.dado == alvo:
                if anterior is None:
                    self.cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self._tamanho -= 1
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
