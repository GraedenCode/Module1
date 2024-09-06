import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do", background_color="Black")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button("Add", button_color="White")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   background_color="Black",
                   font=('Helvetica',20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()