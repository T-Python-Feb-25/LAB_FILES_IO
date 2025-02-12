import json
from datetime import datetime

TODO_FILE = "todo_list.json"

def load_tasks():
    """Load tasks from the JSON file."""
    try:
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(title, date_time):
    """Add a new task to the list."""
    tasks = load_tasks()
    task = {
        "title": title,
        "date_time": date_time,
        "done": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def display_tasks():
    """Display all tasks in the to-do list."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    
    for idx, task in enumerate(tasks, start=1):
        status = "DONE" if task["done"] else "NOT DONE"
        print(f"{idx}- {task['title']} - {task['date_time']} - {status}")

def mark_task_done(task_number):
    """Mark a specific task as done."""
    tasks = load_tasks()
    
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as DONE!")
    else:
        print("Invalid task number.")

def search_task(keyword):
    """Search for tasks by title."""
    tasks = load_tasks()
    filtered_tasks = [task for task in tasks if keyword.lower() in task["title"].lower()]
    
    if filtered_tasks:
        for idx, task in enumerate(filtered_tasks, start=1):
            status = "DONE" if task["done"] else "NOT DONE"
            print(f"{idx}- {task['title']} - {task['date_time']} - {status}")
    else:
        print("No matching tasks found.")

# Example Usage
if  __name__ == "_main_":
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Done")
        print("4. Search Tasks")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Enter task title: ")
            date_time = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            add_task(title, date_time)
        
        elif choice == "2":
            display_tasks()
        
        elif choice == "3":
            task_number = int(input("Enter task number to mark as done: "))
            mark_task_done(task_number)
        
        elif choice == "4":
            keyword = input("Enter search keyword: ")
            search_task(keyword)
        
        elif choice == "5":
            print("Exiting...")
            break
        
        else:
           print("Invalid choice, try again.")