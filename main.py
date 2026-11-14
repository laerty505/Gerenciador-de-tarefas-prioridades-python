import sys
import os
sys.path.append(os.path.abspath('/src/interface.py'))
sys.path.append(os.path.abspath('/src/gerenciador.py'))
sys.path.append(os.path.abspath('/src/estruturas/fila.py'))
import interface
import gerenciador
from estruturas.fila import Fila

tarefas = Fila()

while True:
    interface.menu()
    interface.selecao()
    try:  # Verifica e trata erros de input
        opcao_usuario = int(input('Digite um número: '))
    except ValueError:
        print('Entrada inválida! Digite um número ou "N" para cancelar.')
        input('Aperte ENTER para continuar...')
        continue

    match opcao_usuario:
        case 1:
            print('Criar Tarefa')
            nome = input('Digite o nome do tarefa: ')
            desc = input("Digite a descrição da tarefa: ")
            try:
                prioridade = int(input("Digite a prioridade do tarefa: (1 = ALTA PRIORIDIADE // 5 = BAIXA PRIORIDIADE)  "))
            except ValueError:
                print("Digite apenas números de 1 a 5.")
                input("Aperte ENTER para continuar...")
                continue
            tarefas.enqueue(gerenciador.cria_tarefa(nome, desc, prioridade))

        case 2:
            print("Editar tarefa")
            gerenciador.listar_tarefas(tarefas)
            try:
                indice = int(input("Digite o índice da tarefa que deseja editar: "))
                prioridade = int(input("Digite a nova prioridade (1 = ALTA PRIORIDADE // 5 = BAIXA PRIORIDADE): "))
            except ValueError:
                print("Digite números válidos.")
                input("Aperte ENTER para continuar...")
                continue
            if prioridade < 1 or prioridade > 5:
                print("Digite uma prioridade de 1 a 5.")
                input("Aperte ENTER para continuar...")
                continue
            nome = input("Digite o novo nome da tarefa: ")
            desc = input("Digite a nova descrição da tarefa: ")
            gerenciador.editar_tarefa(tarefas, indice, nome, desc, prioridade)
        case 3:
            print("Excluir tarefas")
            try:
                indice = int(input("Digite o indice do tarefa: "))
            except ValueError:
                print("Digite um número válido")
                input("Aperte ENTER para continuar...")
                continue
            gerenciador.excluir_tarefa(tarefas, indice)
        case 4:
            print('Listar tarefas')
            gerenciador.listar_tarefas(tarefas)
        case 5:
            break
        case _:
            print('Digite um número válido!')
