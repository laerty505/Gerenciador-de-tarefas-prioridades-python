import json
from pathlib import Path
from src.estruturas.lista_encadeada import ListaEncadeada
from src.estruturas.minHeap import MinHeap


def cria_tarefa(nome, descricao, prioridade):
    """Valida e normaliza os campos de uma tarefa."""
    if not isinstance(nome, str) or not isinstance(descricao, str):
        raise ValueError("Nome e descrição devem ser textos.")
    nome = nome.strip()
    descricao = descricao.strip()

    if not nome:
        raise ValueError("O nome da tarefa não pode ficar vazio.")
    if not descricao:
        raise ValueError("A descrição da tarefa não pode ficar vazia.")
    if isinstance(prioridade, bool) or not isinstance(prioridade, int) or not 1 <= prioridade <= 5:
        raise ValueError("A prioridade deve ser um número inteiro de 1 a 5.")

    return {"nome": nome, "descricao": descricao, "prioridade": prioridade}


def carregar_tarefas(caminho):
    """Lê e valida tarefas armazenadas em um arquivo JSON."""
    caminho = Path(caminho)
    try:
        with caminho.open("r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        return []

    if not isinstance(dados, list):
        raise ValueError("O arquivo de tarefas deve conter uma lista JSON.")

    tarefas = []
    for tarefa in dados:
        if not isinstance(tarefa, dict):
            raise ValueError("Cada tarefa no arquivo deve ser um objeto JSON.")
        try:
            tarefas.append(cria_tarefa(
                tarefa["nome"], tarefa["descricao"], tarefa["prioridade"]
            ))
        except KeyError as erro:
            raise ValueError(f"Campo ausente na tarefa: {erro.args[0]}.") from erro
    return tarefas


def salvar_tarefas(lista, caminho):
    """Salva as tarefas pendentes preservando a ordem de chegada."""
    caminho = Path(caminho)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    temporario = caminho.with_name(f"{caminho.name}.tmp")
    with temporario.open("w", encoding="utf-8") as arquivo:
        json.dump(_tarefas_em_ordem_de_chegada(lista), arquivo, ensure_ascii=False, indent=2)
        arquivo.write("\n")
    temporario.replace(caminho)


def carregar_concluidas(caminho):
    """Carrega tarefas concluídas para uma lista encadeada."""
    lista = ListaEncadeada()
    for tarefa in carregar_tarefas(caminho):
        lista.inserir_fim(tarefa)
    return lista


def salvar_concluidas(lista, caminho):
    """Salva em JSON os dados da lista de tarefas concluídas."""
    caminho = Path(caminho)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    temporario = caminho.with_name(f"{caminho.name}.tmp")
    tarefas = []
    atual = lista.cabeca
    while atual is not None:
        tarefas.append(atual.dado)
        atual = atual.proximo
    with temporario.open("w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=2)
        arquivo.write("\n")
    temporario.replace(caminho)


def concluir_tarefa(lista, concluidas, indice):
    """Move a tarefa escolhida para o final da lista de concluídas."""
    ordenadas = _tarefas_por_prioridade(lista)
    if lista.tamanho() == 0:
        print("Não há tarefas pendentes.")
    elif not isinstance(indice, int) or isinstance(indice, bool) or not 1 <= indice <= lista.tamanho():
        print("Índice inválido.")
    else:
        tarefa = ordenadas[indice - 1]
        lista.remover_identidade(tarefa)
        concluidas.inserir_fim(tarefa)
        print(f"Tarefa '{tarefa['nome']}' marcada como concluída.")
        return tarefa
    return None


def listar_concluidas(lista):
    """Exibe as tarefas concluídas na ordem em que foram finalizadas."""
    atual = lista.cabeca
    if atual is None:
        print("Não há tarefas concluídas.")
        return
    indice = 1
    while atual is not None:
        tarefa = atual.dado
        print(f"{indice}. {tarefa['nome']} — {tarefa['descricao']} (prioridade {tarefa['prioridade']})")
        atual = atual.proximo
        indice += 1


def listar_tarefas(lista):
    """Exibe as tarefas pendentes ordenadas por prioridade."""
    if lista.tamanho() == 0:
        print("Não há tarefas pendentes.")
    else:
        for i, tarefa in enumerate(_tarefas_por_prioridade(lista), start=1):
            print(
                f"{i}. {tarefa['nome']} — {tarefa['descricao']} "
                f"(prioridade {tarefa['prioridade']})"
            )
    return lista


def _tarefas_em_ordem_de_chegada(lista):
    """Converte os nós da lista em uma lista Python na ordem original."""
    tarefas = []
    atual = lista.cabeca
    while atual is not None:
        tarefas.append(atual.dado)
        atual = atual.proximo
    return tarefas


def _tarefas_por_prioridade(lista):
    """Retorna tarefas por prioridade, preservando empates por chegada."""
    heap = MinHeap()
    for indice, tarefa in enumerate(_tarefas_em_ordem_de_chegada(lista)):
        # O índice desempata prioridades iguais e evita comparar dicionários.
        heap.inserir((tarefa["prioridade"], indice, tarefa))
    ordenadas = []
    while heap.heap:
        _, _, tarefa = heap.extrair_minimo()
        ordenadas.append(tarefa)
    return ordenadas


def excluir_tarefa(lista, indice):
    """Exclui a tarefa indicada pelo índice da listagem priorizada."""
    ordenadas = _tarefas_por_prioridade(lista)
    if lista.tamanho() == 0:
        print("Não há tarefas pendentes.")
    elif not isinstance(indice, int) or isinstance(indice, bool) or not 1 <= indice <= lista.tamanho():
        print("Índice inválido.")
    else:
        tarefa = ordenadas[indice - 1]
        lista.remover_identidade(tarefa)
        print(f"Tarefa '{tarefa['nome']}' excluída com sucesso.")
    return lista


def editar_tarefa(lista, indice, nome, descricao, prioridade):
    """Atualiza os dados da tarefa indicada na listagem priorizada."""
    ordenadas = _tarefas_por_prioridade(lista)
    if lista.tamanho() == 0:
        print("Não há tarefas pendentes.")
    elif not isinstance(indice, int) or isinstance(indice, bool) or not 1 <= indice <= lista.tamanho():
        print("Índice inválido.")
    else:
        tarefa_original = ordenadas[indice - 1]
        posicao = next(i for i, tarefa in enumerate(_tarefas_em_ordem_de_chegada(lista)) if tarefa is tarefa_original)
        lista.definir(posicao, cria_tarefa(nome, descricao, prioridade))
        print("Tarefa editada com sucesso.")
    return lista
