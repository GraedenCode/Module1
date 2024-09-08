import FreeSimpleGUI as sg
from func import extract_archive

# layout

sg.theme("DarkPurple4")

zip_label = sg.Text("Choose a File to Extract")
zip_input = sg.Input()
zip_button = sg.FileBrowse('Browse', key='File')

destination_label = sg.Text("Choose a Destination Folder")
destination_input = sg.Input()
destination_button = sg.FolderBrowse('Browse', key='Destination')

extract_button = sg.Button('Extract', key='Extract')
output_label = sg.Text(key='Output', text_color='green')

window = sg.Window('File Extractor',
                   layout=[[zip_label,zip_input,zip_button],
                           [destination_label,destination_input,destination_button],
                           [extract_button, output_label]])

while True:
    event, values = window.read()
    archivepath = values["File"]
    dest_dir = values['Destination']
    extract_archive(archivepath, dest_dir)
    window["Output"].update(value='Extraction Completed!')

window.close()