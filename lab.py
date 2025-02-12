
while True:
    userAnswer:str = input("Do You Want To Add A New To-Do Item? (Y or N): ").lower()

    if userAnswer == "y":
        userToDo = input("Add your new To-Do item:")
        with open("Lab_FILES_IO/to_do.txt","a",encoding="UTF-8") as toDofile:
            toDofile.write(userToDo + "\n")
    elif userAnswer == "n":
        userAnswer = input("Do you want to list your To-Do items? (Y or N): ").lower()
        if userAnswer == "y":
            with open("Lab_FILES_IO/to_do.txt","r",encoding="UTF-8") as toDofile:
                items =toDofile.read()
                print(items)
        else:
            print("Thank You")
    elif userAnswer == "exit":
        break
