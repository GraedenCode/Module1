import FreeSimpleGUI as Sg
import ConverterFunctions as Cf
from Bonuses.ConverterGUI.ConverterFunctions import feet_to_inches

feet_label = Sg.Text("Enter Feet:")
feet_input = Sg.Input( key="feet")

inches_label = Sg.Text("Enter Inches:")
inches_input = Sg.Input(key='inches')

convert_button = Sg.Button("Convert")
output_label = Sg.Text(key='output')

window = Sg.Window("Converter", layout=[[feet_label, feet_input],
                                        [inches_label,inches_input],
                                        [convert_button,output_label]])


while True:
    event, values = window.read()
    match event:
        case 'Convert':
            inches = Cf.feet_to_inches(values['feet'], values['inches'])
            window['output'].update(value=inches)
        case Sg.WIN_CLOSED:
            break


window.close()