import json
from pathlib import Path
from src.estruturas.lista_encadeada import ListaEncadeada


def cria_tarefa(nome, descricao, prioridade):
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


def salvar_tarefas(fila, caminho):
    caminho = Path(caminho)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    temporario = caminho.with_name(f"{caminho.name}.tmp")
    with temporario.open("w", encoding="utf-8") as arquivo:
        json.dump(fila.elementos, arquivo, ensure_ascii=False, indent=2)
        arquivo.write("\n")
    temporario.replace(caminho)


def carregar_concluidas(caminho):
    lista = ListaEncadeada()
    for tarefa in carregar_tarefas(caminho):
        lista.inserir_fim(tarefa)
    return lista


def salvar_concluidas(lista, caminho):
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


def concluir_tarefa(fila, concluidas, indice):
    if fila.is_empty():
        print("Não há tarefas na fila.")
    elif not isinstance(indice, int) or isinstance(indice, bool) or not 1 <= indice <= fila.size():
        print("Índice inválido.")
    else:
        tarefa = fila.elementos.pop(indice - 1)
        concluidas.inserir_fim(tarefa)
        print(f"Tarefa '{tarefa['nome']}' marcada como concluída.")
        return tarefa
    return None


def listar_concluidas(lista):
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


def listar_tarefas(fila):
    if fila.is_empty():
        print("Não há tarefas na fila.")
    else:
        for i, tarefa in enumerate(fila.elementos, start=1):
            print(
                f"{i}. {tarefa['nome']} — {tarefa['descricao']} "
                f"(prioridade {tarefa['prioridade']})"
            )
    return fila


def excluir_tarefa(fila, indice):
    if fila.is_empty():
        print("Não há tarefas na fila.")
    elif not isinstance(indice, int) or isinstance(indice, bool) or not 1 <= indice <= fila.size():
        print("Índice inválido.")
    else:
        tarefa = fila.elementos.pop(indice - 1)
        print(f"Tarefa '{tarefa['nome']}' excluída com sucesso.")
    return fila


def editar_tarefa(fila, indice, nome, descricao, prioridade):
    if fila.is_empty():
        print("Não há tarefas na fila.")
    elif not isinstance(indice, int) or isinstance(indice, bool) or not 1 <= indice <= fila.size():
        print("Índice inválido.")
    else:
        fila.elementos[indice - 1] = cria_tarefa(nome, descricao, prioridade)
        print("Tarefa editada com sucesso.")
    return fila
