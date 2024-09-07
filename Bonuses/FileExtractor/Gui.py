import FreeSimpleGUI as sg

# layout

sg.theme("DarkPurple4")

zip_label = sg.Text("Choose a File to Extract")
zip_input = sg.Input()
zip_button = sg.FileBrowse('Browse')

destination_label = sg.Text("Choose a Destination Folder")
destination_input = sg.Input()
destination_button = sg.FolderBrowse('Browse')

extract_button = sg.Button('Extract')

window = sg.Window('File Extractor', layout=[[zip_label,zip_input,zip_button],
                                             [destination_label,destination_input,destination_button]])
while True:
    window.read()
    window.close()