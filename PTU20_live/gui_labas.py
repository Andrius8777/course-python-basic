import PySimpleGUI as sg

layout = [
    [sg.Text("Failo kelias c:/?", font="Broadway 25")],
    [sg.Input(key="-Ivestis-", font="Terminal 15")],
    [
        sg.Button("Ikelti PDF faila", key="Failas ikeltas"), 
        sg.Button("Ikelti sablona", key="Sablonas ikeltas"),
        sg.Button("Start", key="Failas sukonvertuotas"),
    ],
    [sg.Text(size=(50, 1), key="-OUTPUT-", font="Terminal 15")],
]

window = sg.Window("Mano pirmoji programa v.01", layout)
sg.DEFAULT_FONT

while True:
    event, values = window.read()
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


#
