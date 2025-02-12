import os
import json
from datetime import datetime

correct_path = r"C:\Users\wjdan\Documents\python4\LAB_FILES_IO"
os.chdir(correct_path)

FILE_NAME = "to_do.json"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump([], file)


def load_tasks():
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def add_task():
    title = input(" Enter task title: ").strip()
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    task = {"title": title, "date_time": date_time, "done": False}
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(" Task Added Successfully!\n")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print(" No tasks found!")
        return

    print("\n TO-DO LIST:")
    for i, task in enumerate(tasks, start=1):
        status = " DONE" if task["done"] else " NOT DONE"
        print(f"{i}- {task['title']} - {task['date_time']} - {status}")
    print()


def mark_task_done():
    tasks = load_tasks()
    if not tasks:
        print(" No tasks found!")
        return

    list_tasks()
    try:
        task_num = int(input(" Enter task number to mark as DONE: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["done"] = True
            save_tasks(tasks)
            print(" Task marked as DONE!\n")
        else:
            print(" Invalid task number!")
    except ValueError:
        print(" Please enter a valid number!")


def search_task():
    tasks = load_tasks()
    keyword = input(" Enter keyword to search for: ").strip().lower()
    found_tasks = [task for task in tasks if keyword in task["title"].lower()]

    if not found_tasks:
        print(" No tasks found with this keyword.")
        return

    print("\n🔍 Search Results:")
    for task in found_tasks:
        status = " DONE" if task["done"] else " NOT DONE"
        print(f"- {task['title']} - {task['date_time']} - {status}")
    print()


def main():
    while True:
        print("\ TO-DO LIST MENU:")
        print("1- Add Task")
        print("2- View Tasks")
        print("3- Mark Task as Done")
        print("4- Search Task")
        print("5- Exit")

        choice = input(" Select an option (1-5): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            mark_task_done()
        elif choice == "4":
            search_task()
        elif choice == "5":
            print(" Thank you for using the To-Do program! Goodbye!")
            break
        else:
            print(" Invalid choice, please try again!")


if __name__ == "__main__":
    main()
