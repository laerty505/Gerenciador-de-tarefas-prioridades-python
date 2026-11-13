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
        case 3:
            pass
        case 4:
            gerenciador.listar_tarefas(tarefas)
        case 5:
            break
        case _:
            print('Digite um número válido!')
