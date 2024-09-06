import FreeSimpleGUI as sg
import shutil

label1 = sg.Text("Select files to compress:")
input1 = sg.Input(key="File")
choose_button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select files to compress:")
input2 = sg.Input(key="Destination")
choose_button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")

window = sg.Window("File Compressor",background_color="black",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button]])

name_input = sg.Input("new_name")
rename_button = sg.Button('Rename')

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Compress':
            new_name = sg.popup_get_text("File Name")
            shutil.make_archive(base_name=new_name,format="zip",
                                root_dir=values['Destination'], base_dir=values['File'])
        case sg.WIN_CLOSED:
            break

window.close()