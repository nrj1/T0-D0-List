import functions
import PySimpleGUI as psg

label = psg.Text("Enter a T0-D0 task:")
input_box = psg.InputText(tooltip="Type here")
add_button = psg.Button("Add")

window = psg.Window("T0-D0 LIST", layout=[[label], [input_box, add_button]])
window.read()
print("Hello")
window.close()
