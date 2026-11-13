import sys
import os
sys.path.append(os.path.abspath('/src/interface.py'))
sys.path.append(os.path.abspath('/src/gerenciador.py'))
import interface
import gerenciador

tarefas = []

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
            prioridade = int(input("Digite a prioridade do tarefa: (1 = ALTA PRIORIDIADE // 5 = BAIXA PRIORIDIADE)  "))
            tarefas.append(gerenciador.cria_tarefa(nome, desc, prioridade))
            print(tarefas)
        case 2:
            print("Editar tarefa")
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
            break
        case _:
            print('Digite um número válido!')
