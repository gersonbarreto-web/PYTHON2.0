lista = []

while True:
    print("\n===Menu de Opções===")
    print("1. Adicionar tarefa")
    print("2. Remover tarefa")
    print("3. Mostrar tarefas")
    print("0. Sair")
    
    
    opcao = input("Escolha uma opção (1, 2, 3 ou 0): ")

    if opcao == "1":
        tarefa = input("Digite a tarefa a ser adicionada: ")
        lista.append(tarefa)
        print(f"Tarefa '{tarefa}' adicionada com sucesso!")

    elif opcao == "2": 
        tarefa = input("Digite a tarefa a ser removida: ")
        if tarefa in lista:
            lista.remove(tarefa)
            print(f"Tarefa '{tarefa}' removida com sucesso!")
        else:
            print(f"Tarefa '{tarefa}' não encontrada na lista.")

    elif opcao == "3":
        if lista:
            print("\n===Lista de Tarefas===")
            for i, tarefa in enumerate(lista, start=1):
                print(f"{i}. {tarefa}")
        else:
            print("A lista de tarefas está vazia.")

   
    elif opcao == "0":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida! Tente novamente.")