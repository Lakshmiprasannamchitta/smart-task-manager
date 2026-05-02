import json
import os

FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

tasks = load_tasks()

# Add Task
def add_task(task):
    priority = "High" if "urgent" in task.lower() else "Normal"
    tasks.append({
        "task": task,
        "priority": priority
    })
    save_tasks(tasks)
    print("Task saved!")

# Show Tasks
def show_tasks():
    if not tasks:
        print("No tasks yet")
        return

    print("\n--- TASK LIST ---")
    for i, t in enumerate(tasks):
        print(f"{i+1}. {t['task']} → {t['priority']}")

# Suggest Task
def suggest_task():
    if not tasks:
        print("No tasks available")
        return

    for t in tasks:
        if t["priority"] == "High":
            print("\n👉 Do this first:", t["task"])
            return

    print("\n👉 Start with:", tasks[0]["task"])

# Count Tasks
def count_tasks():
    print("\nTotal tasks:", len(tasks))


# 🔥 Run Program
while True:
    print("\n1. Add Task")
    print("2. Show Tasks")
    print("3. Suggest Task")
    print("4. Count Tasks")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        suggest_task()

    elif choice == "4":
        count_tasks()

    elif choice == "5":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice")