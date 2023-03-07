from functions import *
import PySimpleGUI as psg

label = psg.Text("Enter a T0-D0 task:")
input_box = psg.InputText(tooltip="Type here", key="todo")
add_button = psg.Button("Add")

listbox = psg.Listbox(values=get_todos(), key='todos', enable_events=True, size=[45, 10])
edit_button = psg.Button("Edit")
complete_button = psg.Button("Complete")
exit_button = psg.Button("Exit")


window = psg.Window("T0-D0 LIST", layout=[[label],
                                          [input_box, add_button],
                                          [listbox, edit_button, complete_button],
                                          [exit_button]],
                    font="Helvetica")

while True:

    event, value = window.read()
    print(event)
    print(value)

    match event:
        case "Add":
            todos = get_todos()
            x = value["todo"] + "\n"
            todos.append(x)

            write_todos(todos)
            window['todos'].update(values=todos)



        case "Edit":
            try:
                todo_to_edit = value['todos'][0]
                new_todo = value["todo"]

                todos = get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                psg.popup("Please select the file", font=("Helvetica", 20))
                #print("Please select the file to be edited first,"\
                #      "followed by typing the new file name that" \
                 #     "replaces the former and then click the Edit button")

        case 'todos':
            window['todo'].update(value=value['todos'][0])

        case 'Complete':
            todos = get_todos()
            y = value['todos'][0]
            print(y)
            todos.remove(y)
            write_todos(todos)
            window['todo'].update(value='')
            window['todos'].update(values=todos)

        case "Exit":
            exit()

        case psg.WIN_CLOSED:
            break






window.close()
#https://github.com/nrj1/T0-D0-List.git