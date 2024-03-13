class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
        else:
            print("Invalid task index.")

    def display_tasks(self):
        print("To-Do List:")
        for i, task in enumerate(self.tasks):
            status = "Done" if task.completed else "Pending"
            print(f"{i + 1}. {task.description} [{status}]")

def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Display Tasks")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            task = Task(description)
            todo_list.add_task(task)
            print("Task added successfully.")
        elif choice == "2":
            index = int(input("Enter task index to mark as completed: ")) - 1
            todo_list.complete_task(index)
            print("Task marked as completed.")
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
