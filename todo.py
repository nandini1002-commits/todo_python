class Task:
    def __init__(self, description):
        self.description = description

class ToDoList:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                tasks = []
                for line in file:
                    tasks.append(Task(line.strip()))
                return tasks
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                file.write(task.description + '\n')

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        self.save_tasks()

    def delete_task(self, index):
        try:
            del self.tasks[index]
            self.save_tasks()
        except IndexError:
            print("Invalid task index.")

    def view_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task.description}")

def main():
    todo_list = ToDoList('todo.txt')

    while True:
        print("\nTO-DO List Menu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            todo_list.view_tasks()
            index = int(input("Enter task index to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()