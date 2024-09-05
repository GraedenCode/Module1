import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do", background_color="Black")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add", button_color="White")

window = sg.Window('My To-Do App', layout=[[label, input_box, add_button]],background_color="Black")
window.read()
print("hello")
window.close()