

print("***********This is to your To Do list***********")

while True:
    choice = input("would you like to add to your to do list?\nY for Yes \nN for No\nE for Exit").lower()
    if choice == "y":
        with open("ToDo.txt", "a+", encoding="utf-8") as file:
            print("enter your to do item:")
            todo = input("○ ")
            file.write(todo+"\n")
    elif choice == "n":
        items=input("do you want to list your To-Do items?\nY for Yes \nN for No").lower()
        with open("ToDo.txt", "r", encoding="utf-8") as file:
            if items=="y":
                listitems=file.read()
                print(listitems)
            if items=="n":
                continue
    elif choice == "e":
        break

print("thank you for using the To-Do program, come back again soon")