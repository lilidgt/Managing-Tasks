# TASK MANAGER
I created this simples task manager with Python. It's a small but fun little project.

This project is a simple **Task Manager** developed in Python, allowing the user to view, add, remove, and mark tasks as completed. The tasks are stored in a text file (`tarefas.txt`) so they can be saved and loaded during future executions of the program.

## Features
- **Display tasks**: Shows all current tasks in the list.
- **Add new task**: Allows the user to add a new task to the list.
- **Remove task**: Removes a task from the list based on its number.
- **Mark task as completed**: Marks an existing task as completed, adding the tag `[COMPLETED]` next to it.
- **Persistent storage**: Tasks are saved in a `tarefas.txt` file, so your progress is maintained between sessions.

## How to Run the Project
1. **Install Python**:
   - Make sure you have Python 3 installed on your system. If not, download the latest version from [python.org](https://www.python.org/downloads/).
2. **Download the code**:
   - Download or clone this repository to your computer.
3. **Run the program**:
   - Navigate to the project directory and run the `task_manager.py` script using Python:
     ```bash
     python task_manager.py
     ```
4. **Interacting with the program**:
   - When the program starts, you will see a menu with the following options:
      ```
        print("1. Mostrar tarefas;")
        print("2. Adicionar nova tarefa;")
        print("3. Remover tarefa;")
        print("4. Marcar tarefa como concluída;")
        print("5. Sair.")
   - Choose an option by entering the corresponding number and follow the instructions.

## Code Structure
The code is divided into several main functions:
- **`load_tasks()`**: Loads tasks from the `tarefas.txt` file, if it exists. Otherwise, it returns an empty list.
- **`save_tasks(tasks)`**: Saves the tasks to the `tarefas.txt` file, overwriting the existing content.
- **`show_tasks(tasks)`**: Displays all tasks in a numbered list, with each task shown on a separate line.
- **`task_manager()`**: The main function that displays the menu, manages user choices, and calls the appropriate functions based on user input.

## Data File
The program creates and uses the `tarefas.txt` file in the directory where the script is run to store tasks. Tasks are saved line by line, and completed tasks are marked with `[COMPLETED]` in the file.

## Potential Improvements
Here are a few ideas for future improvements:
- Add an option to edit an existing task.
- Implement a category system to better organize tasks.
- Sort tasks by creation date or priority.

Thanks!
