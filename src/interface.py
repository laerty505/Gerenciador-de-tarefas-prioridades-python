import os

def menu():
    """Mostra o título do programa."""
    print("============")
    print("TASK MANAGER")
    print("============")


def selecao():
    """Apresenta as operações disponíveis no menu."""
    print("Digite 1 para criar uma tarefa")
    print("Digite 2 para editar uma tarefa")
    print("Digite 3 para excluir uma tarefa")
    print("Digite 4 para listar todas as tarefas")
    print("Digite 5 para marcar uma tarefa como concluída")
    print("Digite 6 para listar tarefas concluídas")
    print("Digite 7 para sair do programa")

def limpar_terminal():
    """Limpa a tela conforme o sistema operacional."""
    os.system('cls' if os.name == 'nt' else 'clear')
