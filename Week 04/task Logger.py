import os
import datetime

log_file = r"D:\Python Weekly\Week 04\tasks.log"

def add_task(task):
       with open(log_file, "a") as f:  # append mode
        f.write(f"[{datetime.datetime.now()}] TASK: {task}\n")
    print("Task added successfully!")

def view_tasks():
        if not os.path.exists(log_file):
        print("No tasks found yet!")
        return
    
    with open(log_file, "r") as f:
        lines = f.readlines()
    
    print("\n=== Saved Tasks ===")
    for line in lines:
        print(line.strip())

def delete_log():
        if os.path.exists(log_file):
        os.remove(log_file)
        print("Task log deleted!")
    else:
        print("No log file found.")

while True:
    print("\n--- Task Logger ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete All Tasks")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        delete_log()

    elif choice == "4":
        print("Goodbye! ")
        break

    else:
        print("Invalid choice, try again.")
