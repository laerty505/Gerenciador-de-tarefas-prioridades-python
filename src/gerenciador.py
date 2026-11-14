def cria_tarefa(nome, descricao, prioridade):
    tarefa = {
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade
    }
    return tarefa

def listar_tarefas(fila):
    if fila.is_empty():
        print("Não há tarefas na fila.")
    else:
        for i, tarefa in enumerate(fila.elementos, start=1):
            print(f"{i}. {tarefa['nome']} — {tarefa['descricao']}")

    return fila

def excluir_tarefa(fila, indice):
    if fila.is_empty():
        print("Não há tarefas na fila.")
    else:
        for i in fila.elementos:
            fila.elementos.pop(indice)

    return fila

def editar_tarefa(fila, indice, nome, descricao, prioridade):
    if fila.is_empty():
        print("Não há tarefas na fila.")
    elif indice < 1 or indice > fila.size():
        print("Índice inválido.")
    else:
        fila.elementos[indice - 1] = cria_tarefa(nome, descricao, prioridade)
        print("Tarefa editada com sucesso.")

    return fila




