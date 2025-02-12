import json

while True:
    userAnswer:str = input("If You Want To Add A New To-Do Item? (Y or N): and If You Want To Search (S): ").lower()

    if userAnswer == "y":
        title = input("Add item title: ")
        time = input("Enter due Date (YYYY-MM-DD HH:MM): ")
        done = False
        allData = {"title": title, "time": time, "done": done}
        try:
            with open("Lab_FILES_IO/to_do.json", "r", encoding="UTF-8") as toDofile:
                jsonList = json.load(toDofile)  
        except (json.JSONDecodeError):
            jsonList = []

        jsonList.append(allData)

        with open("Lab_FILES_IO/to_do.json", "w", encoding="UTF-8") as toDofile:
            json.dump(jsonList, toDofile)
            print("Added")
    elif userAnswer == "n":
        userAnswer = input("Do you want to list your To-Do items? (Y or N) or modify task ststus press(M): ").lower()
        if userAnswer == "y":
            with open("Lab_FILES_IO/to_do.json","r",encoding="UTF-8") as toDofile:
                reading = json.load(toDofile)
                for dicItem in reading:
                    print(f"{dicItem["title"]} - {dicItem["time"]} - {dicItem["done"]}")
        elif userAnswer == "m":
            with open("Lab_FILES_IO/to_do.json","r",encoding="UTF-8") as toDofile:
                reading = json.load(toDofile)
                userAnswer = input("Choose the to do: ")
                found = False
                for dicItem in reading:
                    if dicItem["title"].lower() == userAnswer.lower():
                            dicItem["done"] = True
                            print(f"Task '{dicItem['title']}' has been marked as done.")
                            break
                with open("Lab_FILES_IO/to_do.json", "w", encoding="UTF-8") as toDofile:
                    json.dump(reading, toDofile)
    elif userAnswer == "s":
        with open("Lab_FILES_IO/to_do.json","r",encoding="UTF-8") as toDofile:
            reading = json.load(toDofile)
            userAnswer = input("What do you want to search for: ")
            found = False
            for dicItem in reading:
                if dicItem["title"].lower() == userAnswer.lower():
                    print(f"Title: {dicItem["title"]}")
                    print(f"Time: {dicItem["time"]}")
                    print(f"Status: {dicItem["done"]}")
                    found = True
                    break
            if not found:
                print("Not Found")
    elif userAnswer == "exit":
        break
    else:
        print("Wrong Input")