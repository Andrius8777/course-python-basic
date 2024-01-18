
try:
    ivestis1 = int(input('Iveskite skaiciu'))
    ivestis2 = int(input('Iveskite skaiciu2'))
    rez = ivestis1 / ivestis2
    print(f'Rezultatas = {rez}')
except ValueError as error:
    print("ivestas neteisingas skaicius", error.__doc__)
except ZeroDivisionError:
    print('Dalyba is nulio negalima')





