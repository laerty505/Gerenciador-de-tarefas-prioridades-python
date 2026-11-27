class MinHeap:
  """Fila de prioridade baseada em um heap mínimo."""

  def __init__(self):
    """Cria um heap inicialmente vazio."""
    self.heap = []

  def _pai(self, i):
    """Calcula o índice do nó pai."""
    return (i - 1) // 2

  def _filho_esq(self, i):
    """Calcula o índice do filho esquerdo."""
    return 2 * i + 1

  def _filho_dir(self, i):
    """Calcula o índice do filho direito."""
    return 2 * i + 2

  def _trocar(self, i, j):
    """Troca de posição dois elementos do heap."""
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

  def inserir(self, item):
    """Insere um item e restaura a propriedade do heap."""
    self.heap.append(item)
    self._subir(len(self.heap) - 1)

  def _subir(self, i):
    """Move um item para cima enquanto for menor que o pai."""
    while i > 0 and self.heap[i] < self.heap[self._pai(i)]:
      pai = self._pai(i)
      self._trocar(i, pai)
      i = pai

  def extrair_minimo(self):
    """Remove e retorna o menor item, ou None se estiver vazio."""
    if not self.heap:
      return None
    if len(self.heap) == 1:
      return self.heap.pop()

    raiz = self.heap[0]
    self.heap[0] = self.heap.pop()
    self._descer(0)
    return raiz

  def _descer(self, i):
    """Move um item para baixo até restaurar a ordem do heap."""
    menor = i
    esq = self._filho_esq(i)
    dir = self._filho_dir(i)
    n = len(self.heap)

    if esq < n and self.heap[esq] < self.heap[menor]:
      menor = esq
    if dir < n and self.heap[dir] < self.heap[menor]:
      menor = dir

    if menor != i:
      self._trocar(i, menor)
      self._descer(menor)

  def __repr__(self):
    """Retorna uma representação textual dos itens armazenados."""
    return str(self.heap)
