import re
import json
def add_to_do_item(dic:dict,title:str):
    '''add new to do list to the file to_do.json if the file dosent exit it will create a new file 
       args:
            dic(dict):a dictionry that contin the to do list the key is the title of the task and the valus is the date and done
            title(String):to check if there is the same title in to do list'''
    try:
        with open("to_do.json","r",encoding="UTF-8") as file:
            data=json.load(file)
    except FileNotFoundError:

        with open("to_do.json","w",encoding="UTF-8") as file:
            json.dump(dic,file,indent=4)
        
    except Exception as e:
        print(e)    
    else:
        if title not in data:
            data.update(dic)
            with open("to_do.json","w",encoding="UTF-8") as file:
                json.dump(data,file,indent=4)
        else:
            print("The title you entered is already in the to-do list.")


            
def display_to_do_items():
    '''display all to do list '''
       
    count=1
    try:
         with open("to_do.json","r",encoding="UTF-8") as file:
            data=json.load(file)
            for key ,value in data.items():
                if data[key]["done"]:
                    done="DONE"
                else:
                    done="NOT DONE"
                print(f"{count}- {key} - {data[key]["date"]} - {done}")
                count+=1
    except Exception as e:
        print(e)
    count=0
def mark_as_done(title:str):
    '''mark specified to do item as done  
       args:
            title(string)The title of the to-do item to mark as done.'''
    with open("to_do.json","r",encoding="UTF-8") as file:
        data=json.load(file)
    if title in data:
    
        data[title]["done"]=True
        with open("to_do.json","w",encoding="UTF-8") as file:
            json.dump(data,file,indent=4)
    else:
        print("The title you entered is not found in the to-do list. Please.")



def search_by_title(title):
    '''print specified to do item by the title  
       args:
            title(string)The title of the to-do item to print.'''
    with open("to_do.json","r",encoding="UTF-8") as file:
        data=json.load(file)
    if title in data:
        if data[title]["done"]:
            done="DONE"
        else:
            done="NOT DONE"
        print(f"{title} - {data[title]["date"]} - {done}")
    else:
        print("The title you entered is not found in the to-do list. Please.")


while True:
    user_input=input("""
If you want to add To_Do list, enter: 1
If you want to print all To do list, enter: 2
If you want to mark title as done, enter: 3
If you want to search by title, enter: 4
If you want to exit, enter: 5
""").strip()
    if user_input.lower()=='1': 
        user_wrating=input("please enter you new To-Do item:")
        user_date_time=input("Enter the date (YYYY-MM-DD HH:MM:SS) in the same format:")
        pattern = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$"
        if re.match(pattern,user_date_time):
            dic={user_wrating:{
                "date":user_date_time,
                "done":False
            }} 
            add_to_do_item(dic,user_wrating)
        else:
            print("Invalid date or time. Please enter a valid date and time.")

    elif user_input=='2':
        
        
         display_to_do_items()
    elif user_input=='3':
            title=input("please enter the title:")
            mark_as_done(title)
    elif user_input=='4':
        title=input("please enter the title:")
        search_by_title(title)

    elif user_input=='5':
        print("thank you for using the To-Do program, come back again soon")
        exit()
    else:
        print("Invalid input, please try again.")
        
