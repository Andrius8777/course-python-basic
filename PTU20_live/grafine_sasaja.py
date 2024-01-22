import PySimpleGUI as sg
from datetime import datetime

dabar = datetime.now()
format_string = "%H:%M:%S"
laikas = dabar.strftime(format_string)

layout = [
    [sg.Text("Failo kelias c:/?", font="Broadway 25")],
    [sg.Text(laikas)],
    [sg.Input(key="-Ivestis-", font="Terminal 15")],
    [
        sg.Button("Ikelti PDF faila", key="Failas ikeltas"), 
        sg.Button("Ikelti sablona", key="Sablonas ikeltas"),
        sg.Button("Start", key="Failas sukonvertuotas"),
    ],
    [sg.Text(size=(50, 1), key="-OUTPUT-", font="Terminal 15")],
]
layout2 = [[sg.Text(laikas)], [sg.Text(size=(50, 1), key="-OUTPUT-", font="Terminal 15")]]

window = sg.Window("Mano pirmoji programa v.01", layout)
window2 = sg.Window("Laikrodis", layout2)
sg.DEFAULT_FONT

while True:
    event, values = window.read()
    event, values = window2.read()
    if event == sg.WINDOW_CLOSED:
        break

    if event == "Failas ikeltas":
        window["-OUTPUT-"].update(
            f"Failas sekmingai pridetas {values['-Ivestis-']}",
        )
    elif event == "Sablonas ikeltas":
        window["-OUTPUT-"].update(
            f"Ikelimas pavyko {values['-Ivestis-']}",
        )
    elif event == "Failas sukonvertuotas":
        window["-OUTPUT-"].update(
            f'Konvertacija pavyko! {'C:/new_folder/'}',
        )

window.close()


