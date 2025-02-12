#user_item:str  = input("input your item: ")
#while True :
 # do_item : str = input("do you want to  add item (write in small letter press y or no):  ")
  #if do_item == 'y':
    # file_item=open("item.txt", "a+" ,encoding="utf-8")
    # file_item.write(user_item)
     #file_item.close()
 # else :
    # more_item= (input ("doy you want to list you item press y or no : "))
    # if more_item == 'y':
       # print(more_item)
    # else:
       # break
     

# To-Do List Program
def add_todo(item):
    """Append a new To-Do item to the file."""
    with open("to_do.txt", "a", encoding="utf-8") as file:
        file.write(item + "\n")

def list_todos():
    """Read and print all To-Do items from the file."""
    try:
        with open("to_do.txt", "r", encoding="utf-8") as file:
            todos = file.readlines()
            if not todos:
                print("Your To-Do list is empty.")
            else:
                print("\nYour To-Do List:")
                for index, todo in enumerate(todos, start=1):
                    print(f"{index}. {todo.strip()}")
    except FileNotFoundError:
        print("No To-Do list found. Start by adding a new item.")


# Main Loop
while True:
    user_input = input("\nDo you want to add a new To-Do item? (y/n) or type 'exit' to quit: ").strip().lower()

    if user_input == "exit":
        print("Thank you for using the To-Do program, come back again soon!")
        break  # Exit the loop
    elif user_input == "y":
        todo_item = input("Enter your new To-Do item: ").strip()
        add_todo(todo_item)
        print("To-Do item added successfully!")

    elif user_input == "n":
        view_list = input("Do you want to list your To-Do items? (y/n): ").strip().lower()
        if view_list == "y":
            list_todos()

    else:
        print("Invalid input. Please enter 'y', 'n', or 'exit'.")