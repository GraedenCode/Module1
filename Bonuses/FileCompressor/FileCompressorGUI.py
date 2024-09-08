import FreeSimpleGUI as sg
from functions import make_archive

sg.theme('DarkGreen4')

label1 = sg.Text("Select files to compress:")
input1 = sg.Input(key="File")
choose_button1 = sg.FilesBrowse("Choose", key='files')

label2 = sg.Text("Select files to compress:")
input2 = sg.Input(key="Destination")
choose_button2 = sg.FolderBrowse("Choose", key='folder')

compress_button = sg.Button("Compress")
output_label = sg.Text(key='Output')

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button,output_label]])

while True:
    event,values = window.read()
    print(event, values)
    filepaths = values['files'].split(';')
    folder = values['folder']
    make_archive(filepaths, folder)
    window['Output'].update(value='Files Zipped!', text_color="Purple")

window.close()