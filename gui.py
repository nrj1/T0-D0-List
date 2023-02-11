from functions import *
import PySimpleGUI as psg

label = psg.Text("Enter a T0-D0 task:")
input_box = psg.InputText(tooltip="Type here", key = "todo")
add_button = psg.Button("Add")
show_button = psg.Button("Show")

window = psg.Window("T0-D0 LIST", layout=[[label], [input_box, add_button], [show_button]],
                    font="Helvetica"
                    )

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

        case psg.WIN_CLOSED:
            break

        case "Show":
            todos = get_todos()
            print(todos)




window.close()
#https://github.com/nrj1/T0-D0-List.git