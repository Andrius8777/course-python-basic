rez_vertes = [0.25, 0.5, 1, 1.5, 2, 3, 5, 10, 20, 50]

def apskaiciavimas(i:float, w:float, u:float):
    rez_vertes = w + (w / 3)
    for index, rez in rez_vertes:
        rez.pop()
        P = i * u
    omai = u / i
    if P > rez_vertes:
        print('Rezistorius sudegs')
    else:
        print(f'{verte}W, {omai} omu')

verte = 2
apskaiciavimas(1, rez_vertes.index(verte), 1)


