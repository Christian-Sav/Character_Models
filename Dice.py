import PySimpleGUI as sg
import random

layout = [  [sg.Text('Roll Some Dice', font='_ 18')],
            [sg.Text('Number of sides'), sg.Combo((4, 6, 8, 12, 10, 20), default_value=6, readonly=True, key='-DICE-')],
            [sg.Text('Number of dice'), sg.Combo((1,2,3,4,5,6,7,8,9,10,11,12), default_value=1, readonly=True, key='-NUM DICE-')],
            [sg.Text('You rolled:', font='_ 18'), sg.Text(key='-ROLLED-', font='_ 18')],
            [sg.Button('Roll')]  ]

window = sg.Window('Dice Roller', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    window['-ROLLED-'].update(' '.join([str(random.randint(0, int(values['-DICE-'])-1)+1) for i in range(int(values['-NUM DICE-']))]))
window.close()
