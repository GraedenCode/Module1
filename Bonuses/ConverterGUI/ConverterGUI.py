import FreeSimpleGUI as Sg
import ConverterFunctions as Cf

feet_label = Sg.Text("Enter Feet:")
feet_input = Sg.Input()

inches_label = Sg.Text("Enter Inches:")
inches_input = Sg.Input()

convert_button = Sg.Button("Convert")

window = Sg.Window("Converter", layout=[[feet_label, feet_input],
                                        [inches_label,inches_input],
                                        [convert_button]])


while True:
    event, values = window.read()
    match event:
        case 'Convert':
            pass
        case Sg.WIN_CLOSED:
            break


window.close()