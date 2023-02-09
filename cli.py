#adding 'to do' fxns as per user's wishes and displaying it
'''query = "Input the number of TO DO activities you want to append to the list:\n"
        ""
n = int(input(query))

list1 = []
task = "Enter tasks to be accomplished: "
for i in range(n):
    k = input(task)
    list1.append(k)
print("The tasks are as follows:-",list1)'''


#File = input("Enter the mothafookin filename which you wish to store the to-do list into (add '.txt' to filename): ")
# todos = []

import time
from functions import *

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ", now)

while True:

    user_action = input("Type 'add' or 'show' or 'edit' or 'complete' or 'exit' ")
    user_action = user_action.strip()

    #match user_action:
        #case "add":
    if user_action.startswith("add"):
        ' todo = input("Enter task to be appended to the todo list") + "\n"'

        todo = user_action[4:] + "\n"


        # file = open('todos.txt', 'r')
        # todos = file.readlines() #It stores the file items in a list and hence
        # file.close()  # we can see the previous values entered in the to do list

        todos = get_todos()


        todos.append(todo)

        # file = open('todos.txt', 'w')
        # file.writelines(todos) #Printing into the file, each list item viz a string in this case,
        # file.close() #is read and \n is taken as new line

        #with open("todos.txt", 'w') as file:
            #file.writelines(todos)
        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()
        print(todos)


        for index,item in enumerate(todos):
            item = item.title()
            #item = item[0:-1]
            item = item.strip('\n')
            print(f"{index + 1}-{item}")

    elif user_action.startswith("edit"):
        no_plus_new_val = user_action[5:]
        #if no_plus_new_val[0].isdigit() is True:
        try:

            todos = get_todos()

        #replacing_index = int(input("Enter which list position is to be edited: "))
        #new_value = input("Enter the new task: ") + "\n"
        #todos[replacing_index - 1] = new_value


            list = no_plus_new_val.split(" ")
            print(list)

            n = len(list)
            new_edited_string = ""
            for i in range(1,n):
                new_edited_string += list[i] + " "



            print(new_edited_string)

            print(list[0])

            x = int(list[0])
            print(type(x))

            todos[x-1] = f"{new_edited_string}\n"
            print(todos)

            write_todos(todos)
            #with open("todos.txt", 'w') as file:
                #file.writelines(todos)

        #else:
        except ValueError:
            print("Invalid Entry! Retry")


    elif user_action.startswith("complete"):
        try:
            todos = get_todos()

            task_no = int(user_action[9:])

            #task_no = int(input("Enter the numbering of the task which has been completed: "))
            todos.pop(task_no - 1)

            write_todos(todos)
            #with open("todos.txt", 'w') as file:
                #file.writelines(todos)
        except ValueError:
            print("Redo the action, we caught an error this time!")




    elif user_action.startswith("exit"):
        break