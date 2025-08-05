# todo.py

TASK_FILE = "tasks.txt"

def load_tasks():
    """Loads tasks from the file and returns a list"""
    try:
        with open(TASK_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Saves the list of tasks to the file"""
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(task):
    """Adds a task to the list"""
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added successfully.")

def view_tasks():
    """Displays all tasks"""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def remove_task(index):
    """Removes a task by index"""
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Task '{removed}' removed.")
    else:
        print("Invalid task number.")

def show_menu():
    """Shows the CLI menu"""
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == "3":
            view_tasks()
            try:
                index = int(input("Enter task number to remove: "))
                remove_task(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")
show_menu()
