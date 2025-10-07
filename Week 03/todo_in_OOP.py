class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_done(self):
        self.completed = True

    def __str__(self):
        status = " Done" if self.completed else " Pending"
        return f"{self.title} - {status}"


class ToDoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        print(f"Task '{title}' added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks yet!")
        else:
            print("\n--- To-Do List ---")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def mark_task_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()
            print(f"Task '{self.tasks[index].title}' marked as done!")
        else:
            print("Invalid task number!")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"Task '{removed.title}' deleted!")
        else:
            print("Invalid task number!")
app = ToDoApp()

while True:
    print("\n--- To-Do App ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == "1":
        title = input("Enter task title: ")
        app.add_task(title)

    elif choice == "2":
        app.view_tasks()

    elif choice == "3":
        app.view_tasks()
        num = int(input("Enter task number to mark as done: ")) - 1
        app.mark_task_done(num)

    elif choice == "4":
        app.view_tasks()
        num = int(input("Enter task number to delete: ")) - 1
        app.delete_task(num)

    elif choice == "5":
        print("Exiting To-Do App. Goodbye! 👋")
        break

    else:
        print("Invalid choice! Try again.")
