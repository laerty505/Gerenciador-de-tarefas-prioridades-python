import json
from pathlib import Path

from src import gerenciador, interface
from src.estruturas.lista_encadeada import ListaEncadeada


ARQUIVO_TAREFAS = Path(__file__).resolve().parent / "tarefas.json"
ARQUIVO_CONCLUIDAS = Path(__file__).resolve().parent / "tarefas_concluidas.json"


def ler_indice(mensagem):
    try:
        return int(input(mensagem))
    except ValueError:
        print("Digite um número inteiro válido.")
        return None


def ler_dados_tarefa(prefixo=""):
    nome = input(f"Digite o nome {prefixo}da tarefa: ")
    descricao = input(f"Digite a descrição {prefixo}da tarefa: ")
    prioridade_texto = input(
        f"Digite a prioridade {prefixo}da tarefa (1 = alta, 5 = baixa): "
    )
    try:
        prioridade = int(prioridade_texto)
        return gerenciador.cria_tarefa(nome, descricao, prioridade)
    except ValueError as erro:
        print(f"Dados inválidos: {erro}")
        return None


def main():
    tarefas = ListaEncadeada()
    try:
        concluidas = gerenciador.carregar_concluidas(ARQUIVO_CONCLUIDAS)
    except (json.JSONDecodeError, ValueError, TypeError) as erro:
        print(f"Não foi possível carregar {ARQUIVO_CONCLUIDAS.name}: {erro}")
        input("Aperte ENTER para sair...")
        return
    try:
        for tarefa in gerenciador.carregar_tarefas(ARQUIVO_TAREFAS):
            tarefas.inserir_fim(tarefa)
    except (json.JSONDecodeError, ValueError, TypeError) as erro:
        print(f"Não foi possível carregar {ARQUIVO_TAREFAS.name}: {erro}")
        print("Corrija o arquivo JSON antes de continuar para evitar perder dados.")
        input("Aperte ENTER para sair...")
        return

    while True:
        interface.limpar_terminal()
        interface.menu()
        interface.selecao()
        opcao = ler_indice("Digite um número: ")
        if opcao is None:
            input("Aperte ENTER para continuar...")
            continue

        try:
            match opcao:
                case 1:
                    interface.limpar_terminal()
                    print("Criar tarefa")
                    tarefa = ler_dados_tarefa()
                    if tarefa is not None:
                        tarefas.inserir_fim(tarefa)
                        gerenciador.salvar_tarefas(tarefas, ARQUIVO_TAREFAS)
                        print("Tarefa criada e salva.")
                    input("Aperte ENTER para continuar...")
                case 2:
                    interface.limpar_terminal()
                    print("Editar tarefa")
                    gerenciador.listar_tarefas(tarefas)
                    indice = ler_indice("Digite o índice da tarefa que deseja editar: ")
                    if indice is not None and 1 <= indice <= tarefas.tamanho():
                        tarefa = ler_dados_tarefa("nova ")
                        if tarefa is not None:
                            gerenciador.editar_tarefa(
                                tarefas, indice, tarefa["nome"], tarefa["descricao"], tarefa["prioridade"]
                            )
                            gerenciador.salvar_tarefas(tarefas, ARQUIVO_TAREFAS)
                    elif indice is not None:
                        print("Índice inválido.")
                    input("Aperte ENTER para continuar...")
                case 3:
                    interface.limpar_terminal()
                    print("Excluir tarefa")
                    gerenciador.listar_tarefas(tarefas)
                    indice = ler_indice("Digite o índice da tarefa que deseja excluir: ")
                    if indice is not None and 1 <= indice <= tarefas.tamanho():
                        gerenciador.excluir_tarefa(tarefas, indice)
                        gerenciador.salvar_tarefas(tarefas, ARQUIVO_TAREFAS)
                    elif indice is not None:
                        gerenciador.excluir_tarefa(tarefas, indice)
                    input("Aperte ENTER para continuar...")
                case 4:
                    interface.limpar_terminal()
                    print("Lista de tarefas")
                    gerenciador.listar_tarefas(tarefas)
                    input("Aperte ENTER para continuar...")
                case 5:
                    interface.limpar_terminal()
                    print("Concluir tarefa")
                    gerenciador.listar_tarefas(tarefas)
                    indice = ler_indice("Digite o índice da tarefa concluída: ")
                    if indice is not None:
                        tarefa = gerenciador.concluir_tarefa(tarefas, concluidas, indice)
                        if tarefa is not None:
                            gerenciador.salvar_concluidas(concluidas, ARQUIVO_CONCLUIDAS)
                            gerenciador.salvar_tarefas(tarefas, ARQUIVO_TAREFAS)
                    input("Aperte ENTER para continuar...")
                case 6:
                    interface.limpar_terminal()
                    print("Tarefas concluídas")
                    gerenciador.listar_concluidas(concluidas)
                    input("Aperte ENTER para continuar...")
                case 7:
                    break
                case _:
                    print("Digite uma opção de 1 a 7.")
                    input("Aperte ENTER para continuar...")
        except OSError as erro:
            print(f"Não foi possível salvar as tarefas: {erro}")
            input("Aperte ENTER para continuar...")


if __name__ == "__main__":
    main()
