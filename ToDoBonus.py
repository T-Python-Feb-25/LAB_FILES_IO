import json

filename = "ToDo_list.json"

def addToDo(title,date,time):
    todolist={}
    try:
        with open(filename ,"r", encoding="utf-8") as file:
            lists = json.load(file)
    except:
        lists = []

    todolist[title] = {
                "date": date,
                "time": time,
                "done": False
            }

    lists.append(todolist)
    with open(filename,"w",encoding="utf-8") as file:
        json.dump(lists,file,indent=4)

def displayList():
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lists = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No to-do list found.")
        return

    e=0
    for i in lists:
        for title, data in i.items():
            e += 1
            if data["done"] == True:
                print(f"{e}- {title} - {data['date']} - {data['time']} - Done ")
            else:
                print(f"{e}- {title} - {data['date']} - {data['time']} - Not Done")


def markDone(num):
    with open(filename, "r", encoding="utf-8") as file:
        lists = json.load(file)

    if 1 <= num <= len(lists):
        task = lists[num - 1]
        title = list(task.keys())[0]
        task[title]["done"] = True
        print(f"Task number {num} is marked Done")

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(lists, file, indent=4)


def searchItem(title):
    with open(filename, "r", encoding="utf-8") as file:
        lists = json.load(file)
        for i in lists:
            for task_title, data in i.items():
                if title.lower() in task_title.lower():
                    if data["done"] == True:
                        print(f"task found- {title} - {data['date']} - {data['time']} - Done ")
                    else:
                        print(f"task found- {title} - {data['date']} - {data['time']} - Not Done")


def main():
    print("*******Welcome to your To Do list items*******")
    while True:
        choice=input("what would you like to do?"
                     "\n(1) add to your to-do list"
                     "\n(2) display your to-do list"
                     "\n(3) mark a task done"
                     "\n(4) search in your to-do list"
                     "\n(5) exit the list"
                     "\nEnter your choice: ")
        if choice == "1":
            title = input("Enter the title of the task: ")
            date = input("Enter the date of the task, in this format: YYYY-MM-DD: ")
            time = input("Enter the time of the task, in this format: HH:MM:SS ")
            addToDo(title,date,time)
        elif choice == "2":
            print("here is your To Do list")
            displayList()
        elif choice == "3":
            number = int(input("Enter the number of the task to mark done: "))
            markDone(number)
        elif choice == "4":
            num = input("Enter the title of the task to search in your to-do list: ")
            searchItem(num)
        elif choice == "5":
            print("Thank you! See you later!❤︎")
            break


if __name__ == "__main__":
    main()