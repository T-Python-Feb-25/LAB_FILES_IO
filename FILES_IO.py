
while True:

    user_in = input("Do you want to add a new To-Do item?")

    if user_in == "y":
        to_do_item = input("What is your new To-Do item? ")
        with open("file_to_do", "a", encoding="utf-8") as file:
            file.write(to_do_item + "\n")
    elif user_in == "n":
        user_in = input("do you want to list your To-Do item ? ")
        if user_in == "y":
            with open("file_to_do", "r", encoding = "utf-8") as file:
                content = file.read()
                print(content)
    elif user_in == "exit":
        break







