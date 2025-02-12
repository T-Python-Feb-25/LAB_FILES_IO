"""
Using what you learned about Python File I/O , we want to make a progeram called To-Do List , this program should do the following:
Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
If the user answers yes , then ask the user to type in his new To-Do item . Then save that To-Do item inside the a file to_do.txt on a new line.
If the user answers no, then ask the user : do you want to list your To-Do items ? answer "y" for yes and "n" for no.
If the user answers yes for reading his To-Do list , then print a list of the To-Do items one item per line.
Then return again to ther first question and ask again, you coninue this untill the user types in "exit" , then you exit the program. and print to the user "thank you for using the To-Do program, come back again soon"

"""
file = open("to_do.txt", "w", encoding="UTF-8")
file.write("new To do  ")    
    
file.close()
while True:
  try:
    user_input = input("add a new To-Do item?")
    if user_input == "y":
      user_To = input("type in your new To-Do item:")
      with open("to_do.txt", "a", encoding="UTF-8") as file:
        file.write(user_To + "\n")
      print("To Do add success")

    elif user_input == "n":
      user_list = input("do you want to list your To-Do items:")

      if user_list == "y":
        try:
          with open("to_do.txt", "r", encoding="UTF-8") as file:
            print(file.read())
        except FileNotFoundError:
          print("file not found")
      
      if user_list == "n":
        print("thank you for using the To-Do program, come back again soon")

    if user_input == "exit":
      print("thank you for using the To-Do program, come back again soon")
      break
  except Exception as e:
    print(f"An error occurred: {e}")



