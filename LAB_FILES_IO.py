def add_to_do_item(to_do_list:str):
    '''add new to do list in the file to_do.txt
       args to_do_list(string):string that will be write in the file'''
    with open("to_do.txt","a+",encoding="UTF-8") as file:
        file.write(user_wrating+"\n")


def display_to_do_items():
    '''print all to do list'''
    try:
         with open("to_do.txt","r",encoding="UTF-8") as file:
            for r in file.readlines():    
                print(r,end="")
    except Exception as e:
        print(e)
    


while True:
    user_input=input("do you want to add a new To-Do item (y or n)? ")
    if user_input.lower()=='y':
        to_do_list=input("please enter you new To-Do item:")

        add_to_do_item(user_wrating)
    elif user_input.lower()=='n':
        user_wrating=input("do you want to list your To-Do items(y or n) ?")
        if user_wrating.lower()=="y":
            display_to_do_items()
    elif user_input.lower()=="exit":
        print("thank you for using the To-Do program, come back again soon")
        exit()
    else:
        print("Invalid input, please try again.")
        
