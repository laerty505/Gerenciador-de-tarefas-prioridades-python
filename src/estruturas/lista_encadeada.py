class No:
    """Armazena um dado e a referência para o próximo nó."""

    def __init__(self, dado):
        """Cria um nó sem sucessor inicial."""
        self.dado = dado
        self.proximo = None


class ListaEncadeada:
    """Lista ligada de nós, usada para tarefas pendentes e concluídas."""

    def __init__(self):
        """Inicializa a lista vazia e seu contador de elementos."""
        self.cabeca = None
        self._tamanho = 0

    def inserir_inicio(self, dado):
        """Adiciona um dado antes do primeiro nó."""
        novo_no = No(dado)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no
        self._tamanho += 1

    def inserir_fim(self, dado):
        """Adiciona um dado depois do último nó."""
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
        """Retorna a quantidade atual de nós."""
        return self._tamanho

    def obter(self, indice):
        """Retorna o dado localizado no índice iniciado em zero."""
        atual = self.cabeca
        for _ in range(indice):
            atual = atual.proximo
        return atual.dado

    def definir(self, indice, dado):
        """Substitui o dado localizado no índice iniciado em zero."""
        atual = self.cabeca
        for _ in range(indice):
            atual = atual.proximo
        atual.dado = dado

    def remover_indice(self, indice):
        """Remove pelo índice e retorna o dado removido."""
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
        """Remove o nó cujo dado é o mesmo objeto indicado."""
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
        """Remove a primeira ocorrência igual ao dado indicado."""
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
        """Informa se existe um dado igual ao valor procurado."""
        atual = self.cabeca
        while atual is not None:
            if atual.dado == alvo:
                return True
            atual = atual.proximo
        return False

    def exibir(self):
        """Retorna os dados da lista em formato encadeado legível."""
        elementos = []
        atual = self.cabeca
        while atual is not None:
            elementos.append(str(atual.dado))
            atual = atual.proximo
        return " -> ".join(elementos) if elementos else "Lista vazia"
