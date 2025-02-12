"""
Modify the project to be able to do the following instead of writing the to do items line by line (hint: use the json module):
each to-do item should be saved with the following attributes:

title
date & time
done (default is false)
User can display his to do list items as follows:

1- Go to Gym - 2023-08-05 08:00:00 - DONE
2- Visit Grandma - 2023-08-08 21:00:00 - NOT DONE
User can mark a specific Task as Done.

User can search in his tasks using the title.


"""
import json
import datetime
import os 
file_name = "to_do.json"

def load_tasks():
  if not os.path.exists(file_name):
    return []
  try:
    with open(file_name, 'r', encoding="UTF-8") as file:
      return json.load(file)
    
  except json.JSONDecodeError as e :
    print("Invalid JSON syntax:", e)
    return []

def save_tasks(tasks):
  with open(file_name, 'w', encoding="UTF-8") as file:
    json.dump(tasks, file, indent=4)

def add_task():
  title = input("Enter the task title:")
  date = input("Enter the date (YYYY-MM-DD %H:%M:%S):")

  try:
    datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
  except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD")
    return 
  
  new_task = {
    "title": title,
    "date": date,
    "done": False
  }
  tasks = load_tasks()
  tasks.append(new_task)
  save_tasks(tasks)
  print("Task added successfully")




def list_tasks():
  tasks = load_tasks()
  if not tasks:
    print("Not fond any list")
  else:
    for i, task in enumerate(tasks, start=1):
      if not task["done"]:
        print(f"{i}. {task['title']} - {task['date']} - 'Not Done '")
      else:
        print(f"{i}. {task['title']} - {task['date']} - 'Done'")
  
def search_taske():
  tasks = load_tasks()
  search = input("Enter the task you want to search for:")
  found = False
  for task in tasks:
    if search.lower() in task["title"].lower():
      print(f"Title {task['title']} - {task['date']} {'Done'  if task['done'] else 'not done'}")
      found = True
      break
  if not found:
      print("Not found")


def update_task():
    tasks = load_tasks()
    print(tasks)
    search = input("Enter the task you want to update:")
    found = False
    for task in tasks:
        if search.lower() in task["title"].lower():
            task["done"] = not task["done"]
            status = "DONE" if task["done"] else "Not done"
            print(f"Task : {task['title']} stauts update is {status}")
            found = True
            break
    if not found:
          print("not exit tasks")
    save_tasks(tasks)

      

while True:
  print("\nTo-Do List Menu")
  print("1. Add new task")
  print("2. List all  tasks")
  print("3. update of task")
  print("4. search_task")
  choice = input("Enter your choice:")
  if choice == "1":
    add_task()

  elif choice == "2":
    list_tasks()
    print('/n------------------')

  elif choice == "3":
    update_task()
    print('/n------------------')

    break
  elif choice == "4":
    search_taske()
    print('/n------------------')

  else:
    print("Invaild choice")

