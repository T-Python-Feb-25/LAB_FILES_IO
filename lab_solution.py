"""# LAB_FILES_IO


## Using what you learned about Python File I/O , we want to make a progeram called To-Do List , this program should do the following:
- Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
- If the user answers yes , then  . 
- If the user answers no, then ask the user : 
- If the user answers yes for reading his To-Do list , then print a list of the To-Do items one item per line.
- Then return again to ther first question and ask again, you coninue this untill the user types in "exit" , then you exit the program. and print to the user "thank you for using the To-Do program, come back again soon"
"""


def input_validation(text:str)->bool:
    if text=="exit":
        return False
    elif text.isalpha() and len(text)==1 and (text.lower()=="n"or text.lower()=="y"):
        return True 
    
    raise TypeError("invalid input ,please write \"y\" for yes and \"n\" for no.")





print("-"*20,"welcome to the TO DO LIST","-"*20)
flag=True
while flag:
    try:
        file= open("to_do.txt","+a",encoding="utf-8")
        user_choice= input("-do you want to add a new To-Do item (\"y\" for yes \"n\" for no) ? ")
        if not input_validation(user_choice):
            flag=False
        #ask the user to type in his new To-Do item
        if(user_choice=="y"):
            new_item=input("Enter the new item: ")
            #Then save that To-Do item inside the a file to_do.txt on a new line.
            file.write(new_item +"\n")
            file.close()
        elif user_choice=="n":
          #  do you want to list your To-Do items ? answer "y" for yes and "n" for no. 
            while True:
                try:
                    check= input("-do you want to list your To-Do items (\"y\" for yes \"n\" for no) ? ")
                    if not input_validation(check):
                        flag=False  
                        break            
                      #reading his To-Do list , then print a list of the To-Do items one item per line.
                    if (check=='y'):
                        print("-"*40)
                        print("To-Do List".center(40))
                        print("-"*40)

                        file.seek(0)
                        content =file.read()
                        print(content)
                        file.close()
                except TypeError as error:
                    print(error)
                else:
                    break
    except TypeError as error:
        print(error)
    except FileNotFoundError:
        print("somthing went wrong pleasr try again later")
    except Exception:
        print("somthing went wrong pleasr try again later")

else:
    print("thank you for using the To-Do program, come back again soon")

        







