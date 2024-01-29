""" Komandinio darbo / savarankiška užduotis
===[ Biudžetas ]===

Reikalavimai

* Biudžeto turinys - pajamų/išlaidų žurnalo žodynas
** raktas - paskirtis
** reikšmė - pajamos pozityvus float, išlaidos negatyvus float
* Galimybė pridėti pajamas arba išlaidas
* Spausdinti pajamų/išlaidų žurnalą
* Suskaičiuoti biudžeto balansą

"""
import os
import pickle


def prideti_iplaukas_islaidas(biudzetas, pavadinimas: str, suma: float):    # 1 Pridėti pajamas arba išlaidas
    if pavadinimas in biudzetas:
        biudzetas[pavadinimas] += suma
    else:
        biudzetas[pavadinimas] = suma
    return biudzetas[pavadinimas]

def finansu_ataskaita(biudzetas):                                        # 2 Spausdinti finansų ataskaitą
    print('Pajamų ir išlaidų žurnalas:')
    for index, (pavadinimas, suma) in enumerate(biudzetas.items(), start=1):
        if suma > 0:
            print(f'{index}. Pajamos ({pavadinimas}): {suma:.2f} €')
        elif suma < 0:
            print(f'{index}. Išlaidos ({pavadinimas}): {suma:.2f} €')
        else:
            print(f'{index}. {pavadinimas}: {suma:.2f} €')

def biudzeto_balansas(biudzetas):                    # 3 Skaičiuoti biudžeto balansą
    balansas = 0
    for suma in biudzetas.values():
        balansas += suma
    return balansas
def main():                #menu inputas
    biudzetas = {}

    while True:
        print('''
        --- Ką norite pasirinkti?:--- 
        0. Nesigadink sau nervų ir išeik     
        1. Pridėti pajamas arba išlaidas
        2. Spausdinti finansų ataskaitą
        3. Skaičiuoti biudžeto balansą
            ''')
        choice = input('Pasirinkite veiksmą (0-3): ')
        
        if choice == '0':
             print('Teisingas sprendimas')
             break
        
        elif choice == "1":
            while True:
                pavadinimas = input('Įveskite kategoriją: ')
                if pavadinimas.isnumeric():
                    print('Pajamų ar išlaidų pavadinimas turi būti žodis!')
                    continue
                else:
                    break
            while True:
                sumos_ivedimas = input('Įveskite sumą (neigiama suma reiškia išlaidas): ')
                try:
                    suma = float(sumos_ivedimas)
                    break
                except ValueError:
                    print('Įvesti duomenys netinka. Prašome įvesti skaičių.')
            prideti_iplaukas_islaidas(biudzetas, pavadinimas, suma)
            print(f'Pridėta: {suma:.2f} € prie kategorijos {pavadinimas}')
        elif choice == "2":
            finansu_ataskaita(biudzetas)
        elif choice == "3":
            balansas = biudzeto_balansas(biudzetas)
            print(f'Biudžeto balansas: {balansas:.2f} €')
        else:
            print("Neteisingas pasirinkimas. Bandykite dar kartą.")


if __name__ == "__main__":
    main()
