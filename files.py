"""Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
If the user answers yes , then ask the user to type in his new To-Do item . Then save that To-Do item inside the a file to_do.txt on a new line.
If the user answers no, then ask the user : do you want to list your To-Do items ? answer "y" for yes and "n" for no.
If the user answers yes for reading his To-Do list , then print a list of the To-Do items one item per line.
Then return again to ther first question and ask again, you coninue this untill the user types in "exit" , then you exit the program. and print to the user "thank you for using the To-Do program, come back again soon"""""



import os

correct_path = r"C:\Users\wjdan\Documents\python4\LAB_FILES_IO"
os.chdir(correct_path)


if not os.path.exists("to_do.txt"):
    with open("to_do.txt", "w", encoding="utf-8") as file:
        file.write("")  

print(" Changed Directory To:", os.getcwd())  




def add_task():
    
    task = input("\n Enter new task : ")
    with open("to_do.txt", "a", encoding="utf-8") as file:
        file.write(task + "\n")
        file.flush()
    print("Added Successfully \n")

def list_tasks():
    
    try:
        with open("to_do.txt", "r", encoding="utf-8") as file:
            tasks = file.readlines()
            if tasks:
                print("\n TO DO LIST:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}- {task.strip()}")
            else:
                print("\n To Do list the empty ")
    except FileNotFoundError:
        print("\n No task file found!")

def main():
    
    while True:
        choice = input("\n Do you want to add a new task? (y/n) or type 'exit' to quit: ").strip().lower()

        if choice == "y":
            add_task()
        elif choice == "n":
            view_choice = input("Do you want to view your to-do list?").strip().lower()
            if view_choice == "y":
                list_tasks()
        elif choice == "exit":
            print("\n Thank you for using the To-Do program Come back again soon!   ")
            break
        else:
            print("\n invalid choice, please try again")

if __name__ == "__main__":
    main()


