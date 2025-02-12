"""# Bonus
## Modify the project to be able to do the following instead of  writing the to do items line by line (**hint**: use the `json` module):
- each to-do item should be saved with the following attributes:
- - title
  - date & time
  - done (default is false)

- User can display his to do list items as follows:
  ```
  1- Go to Gym - 2023-08-05 08:00:00 - DONE
  2- Visit Grandma - 2023-08-08 21:00:00 - NOT DONE
  ```
- User can mark a specific Task as Done.
- User can search in his tasks using the title.
"""

from datetime import datetime
import json

def display_list():
  
    
    items =load_items(file_name)
    if len(items)==0:
        print("**No Tasks added**")
        return
    print("-"*40)
    print("Your current Tasks".center(40))
    print("-"*40)
    for index,item in enumerate(items,start=1):    
        is_done="Done" if item["done"] else "NOT DONE"
        print(f"{index}- {item["title"]} - {item["date"]} -{is_done}")

def date_validation()->str:
    valid = False
    date_format = "%Y-%m-%d %H:%M:%S"
    
    while not valid:
        date_input = input("Enter the date and time (YYYY-MM-DD HH:MM:SS): ")
        try:
            datetime.strptime(date_input, date_format)
            valid = True 
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD  HH:MM:SS.")
    return date_input

def load_items(filename)->list:
    try:
        with open(filename, "r", encoding="utf-8") as json_file:
            return json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        return [] 

def save_items(filename, items):
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(items, json_file, indent=4)

def add_item():
    new_item = input("Enter the new task: ")
    date_time = date_validation()  
    completion = False
    item = {"title": new_item, "date": date_time, "done": completion}

    items = load_items(file_name)  
    items.append(item)  
    save_items(file_name, items)  

def update_task(index :int):
    items=load_items(file_name)
    if index<=len(items):
        items[index-1]['done']= True if not items[index-1]['done'] else False
        is_done="Done" if items[index-1]['done'] else "NOT DONE"
        save_items(file_name,items)
        print(f"the status of task ({items[index-1]['title']}) has been updated successfully to {is_done}")
    else:
        print("the number is not on the list please try again..")

def search(title:str):
    items=load_items(file_name)
    found=False
    for item in items:   
        if(title==item["title"]):
            is_done="Done" if item["done"] else "NOT DONE"
            print(f"Your Task {item["title"]} - {item["date"]} -{is_done}")
            found=True
    if not found:
        print("this task was not found")

file_name="to_do.json"

print("-"*15,"welcome to the TO DO LIST","-"*15)
menu='''---------------------------------------------------------
    1- Display the Tasks 
    2- Add new Task
    3- update Task status
    4- Search for a task
    5- exit
---------------------------------------------------------
'''
flag=True
while flag:
    try:
        user_choice= input(menu+"\nEnter your choice:")
        print()
        if(user_choice=="1"):
            display_list()
            input()
        elif user_choice=="2":
            add_item()
            print("The task has been added successfully")
        elif user_choice=="3":
            display_list()
            valid = True
            while valid:
                number_task= input("please enter the task number that you want to update: ")
                if (number_task.isdigit()):
                    update_task(int(number_task))
                    valid=False
                else:
                    print("invalid input, Enter numbers only")
        elif user_choice=="4":
            task_title= input("please enter the task title that you want to search for: ")
            search(task_title)
            input()
        elif user_choice=="5":
            flag=False
        else:
            raise TypeError("invalid input, Enter numbers only") 
    except TypeError as error:
        print(error)
    except Exception as err:
        print("somthing went wrong please try again later")
else:
    print("thank you for using the To-Do program, come back again soon")

        







