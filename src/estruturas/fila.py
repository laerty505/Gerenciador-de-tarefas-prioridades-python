class Fila:
    def __init__(self):
        self.elementos = []

    def enqueue(self, item):
        """Adiciona um elemento ao final da fila."""
        self.elementos.append(item)

    def dequeue(self):
        """Remove e retorna o primeiro elemento da fila."""
        if self.is_empty():
            raise IndexError("A fila está vazia.")
        return self.elementos.pop(0)

    def peek(self):
        """Retorna o primeiro elemento sem removê-lo."""
        if self.is_empty():
            raise IndexError("A fila está vazia.")
        return self.elementos[0]

    def is_empty(self):
        """Verifica se a fila não possui elementos."""
        return len(self.elementos) == 0

    def size(self):
        """Retorna o número de elementos na fila."""
        return len(self.elementos)

