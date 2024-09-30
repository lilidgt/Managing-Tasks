#permite criar o arquivo tarefas.txt
import os

tasks_archive = 'tarefas.txt'

#carrega tarefas do tarefas.txt
def load_tasks():
    if os.path.exists(tasks_archive):
        with open(tasks_archive, 'r') as archive:
            tasks = [line.strip() for line in archive.readlines()]
    else:
        tasks = []
    return tasks

#salva tarefas no arquivo
def save_tasks(tasks):
    with open(tasks_archive, 'w') as archive:
        for task in tasks:
            archive.write(task + '\n')

#exibe a lista de tarefas
def show_tasks(tasks):
    print("\nTarefas:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()

#principal
def task_manager():
    tasks = load_tasks()

    while True:
        print("\nGERENCIADOR DE TAREFAS:")
        print("1. Mostrar tarefas;")
        print("2. Adicionar nova tarefa;")
        print("3. Remover tarefa;")
        print("4. Marcar tarefa como concluída;")
        print("5. Sair.")

        option = input("Escolha uma opção (1-5): ")

        if option == '1':
            show_tasks(tasks)

        elif option == '2':
            new_task = input("Digite a nova tarefa: ")
            tasks.append(new_task)
            save_tasks(tasks)
            print(f"Tarefa '{new_task}' adicionada.")

        elif option == '3':
            show_tasks(tasks)
            try:
                num_task = int(input("Digite o número da tarefa que deseja remover: "))
                if 1 <= num_task <= len(tasks):
                    removed_task = tasks.pop(num_task - 1)
                    save_tasks(tasks)
                    print(f"Tarefa '{removed_task}' removida. :(")
                else:
                    print("Número de tarefa inválido. >:(")
            except ValueError:
                print("Por favor, insira um número válido. >:(")

        elif option == '4':
            show_tasks(tasks)
            try:
                num_task = int(input("Digite o número da tarefa que deseja marcar como concluída: "))
                if 1 <= num_task <= len(tasks):
                    finished_task = tasks[num_task - 1] + " [CONCLUÍDA]"
                    tasks[num_task - 1] = finished_task
                    save_tasks(tasks)
                    print(f"Tarefa '{finished_task}' marcada como concluída. UHUL! VIVA A PROATIVIDADE! :D")
                else:
                    print("Número de tarefa inválido. >:(")
            except ValueError:
                print("Por favor, insira um número válido. >:(")

        elif option == '5':
            print("Saindo do gerenciador de tarefas... Tchau! :)")
            break

        else:
            print("Opção inválida, por favor escolha entre 1 e 5.")

if __name__ == "__main__":
    task_manager()
