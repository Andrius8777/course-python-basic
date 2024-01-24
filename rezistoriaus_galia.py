print("---REZISTORIAUS GALIOS(W) SKAICIUOKLE----")
srove = float(input('Iveskite kokios stiprumo srove(I) amperais tekes grandineja?:'))
itampa = float(input('Iveskite itampos(U) verte voltais: '))
galia = float(input('Iveskite rezistoriaus galia(W):'))
rezistoriaus_limitas = galia + (galia / 3) #esant tokiomis salygomis rezistoriaus galia turetu buti -+30% daugiau
galios_formule = srove * itampa
omai = itampa / srove
print(f'Jusu naudojama srove(I) amperais yra: {srove}A.')
print(f'Jusu numatoma naudoti rezistoriaus galia yra: {galia}W.')
print(f'Jusu darbine itampa(U) yra: {itampa}V.')
if rezistoriaus_limitas > galios_formule:
    print(f'Jusu rezistoriaus verte: {galia}W pasirinkta tinkamai ir Jums deretu rinktis {omai}\u03A9 rezistoriu!')
else:
    print(f'Rezistoriaus galia {galia}W pasirinkta per maza: rezistorius tiesiog sudegs')