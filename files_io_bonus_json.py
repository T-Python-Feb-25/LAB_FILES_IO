import json
from datetime import datetime

# دالة لإضافة مهمة جديدة
def add_task(title):
    task = {
        'title': title,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'done': False
    }

    try:
        with open("to_do.json", "r", encoding="UTF-8") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

    tasks.append(task)

    with open("to_do.json", "w", encoding="UTF-8") as file:
        json.dump(tasks, file, indent=4)
    print("Task added successfully!")

# دالة لعرض المهام
def display_tasks():
    try:
        with open("to_do.json", "r", encoding="UTF-8") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("No To-Do list found. Start by adding a task.")
        return

    if tasks:
        for index, task in enumerate(tasks, 1):
            status = "DONE" if task['done'] else "NOT DONE"
            print(f"{index}- {task['title']} - {task['date']} - {status}")
    else:
        print("Your To-Do list is empty.")

   # دالة المهمه المكتمله
def mark_task_done(task_number):
    try:
        with open("to_do.json", "r", encoding="UTF-8") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("No To-Do list found. Start by adding a task.")
        return

    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['done'] = True
        with open("to_do.json", "w", encoding="UTF-8") as file:
            json.dump(tasks, file, indent=4)
        print(f"Task {task_number} marked as DONE.")
    else:
        print("Invalid task number.")

# دالة البحث في المهام
def search_task(title):
    try:
        with open("to_do.json", "r", encoding="UTF-8") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("No To-Do list found. Start by adding a task.")
        return

    found = False
    for index, task in enumerate(tasks, 1):
        if title.lower() in task['title'].lower():
            status = "DONE" if task['done'] else "NOT DONE"
            print(f"{index}- {task['title']} - {task['date']} - {status}")
            found = True
    
    if not found:
        print("No tasks found with that title.")

while True:
    user_IO = input("Do you want to add a new To-Do item? Answer 'y' for yes, 'n' for no, or type 'exit' to quit: ").strip().lower()

    if user_IO == "y":
        new_item = input("Enter your new To-Do item: ").strip()
        add_task(new_item)

    elif user_IO == "n":
        display_tasks()

        delete = input("\nDo you want to mark a task as done? (y/n): ").strip().lower()
        if delete == "y":
            try:
                task_num = int(input("Enter the task number to mark as done: ").strip())
                mark_task_done(task_num)
            except ValueError:
                print("Please enter a valid number.")

        search = input("\nDo you want to search for a task by title? (y/n): ").strip().lower()
        if search == "y":
            search_title = input("Enter the title to search: ").strip()
            search_task(search_title)

    elif user_IO == "exit":
        print("Thank you for using the To-Do program, come back again soon!")
        break

    else:
        print("Invalid input, please enter 'y', 'n', or 'exit'.")


