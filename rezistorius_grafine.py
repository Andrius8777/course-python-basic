import PySimpleGUI as sg

rez_vertes = [0.25, 0.5, 1, 1.5, 2, 3, 5, 10, 20, 50]
omai = 0
def apskaiciavimas(i:float, w:float, u:float):
    P = i * u
    rez_vertes = w + (w / 3)
    omai = u / i
    if P > rez_vertes:
        print('Rezistorius sudegs')
    else:
        print(f'Galia(w): {rez_vertes}, omai: {omai}')
    


layout = [
    [sg.Text("Srove(I) amperais:", size=20), sg.Input('0', key="-SROVE-", justification="right", size=10)],
    [sg.Text("Itampa(U) voltais:", size=20), sg.Input('0',key="-ITAMPA-", justification="right", size=10)],
    [sg.Text("Rezistoriaus galia(W):", size=20), sg.Combo(values=rez_vertes, size=(10, 10), key='-rez_sarasas-')],
    [sg.Text("Rezistoriaus varza(\u03A9):", size=20), sg.Text(omai, key='-Omai-', justification="right", size=9)],
    [sg.Text("Galia(W)", size=10), sg.Text("", key="-ATSAKYMAS", justification="right", size=10)],
]

window = sg.Window("GALIOS SKAICIUOKLE", layout, font="Serif 20")
ats = 0

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == "Atsakymas":
        ats = apskaiciavimas(values, window)




window.close()
