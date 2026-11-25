import os

def menu():
    print("============")
    print("TASK MANAGER")
    print("============")


def selecao():
    print("Digite 1 para criar uma tarefa")
    print("Digite 2 para editar uma tarefa")
    print("Digite 3 para excluir uma tarefa")
    print("Digite 4 para listar todas as tarefas")
    print("Digite 5 para marcar uma tarefa como concluída")
    print("Digite 6 para listar tarefas concluídas")
    print("Digite 7 para sair do programa")

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
