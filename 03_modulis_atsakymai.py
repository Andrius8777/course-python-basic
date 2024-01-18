#Pirma užduotis
#Sukurkite naują katalogą pavadinimu "Mano_Katalogas"
# dabartinėje darbo vietoje. Patikrinkite, ar
# katalogas buvo sėkmingai sukurtas,
# ir atspausdinkite rezultatą.

import os
katalogo_kelias = 'Ptu20_live/Mano_Katalogas'
if not os.path.exists(katalogo_kelias):
    os.makedirs('Mano_Katalogas')

#Antra užduotis
#Parašykite programą, kuri peržiūrėtų dabartinį darbo
#katalogą ir atspausdintų visus rastus failus
# bei katalogus.
    
katalogo_kelias = '.'
turinys = os.listdir(katalogo_kelias)
print("Mano katalogas")
for info in turinys:
    print(info)



#Sukurkite naują failą pavadinimu "testas.txt" 
#dabartinėje darbo vietoje. Tada parašykite programą, 
#kuri patikrintų, ar failas "testas.txt" egzistuoja,
#ir trintų jį, jei egzistuoja. Atspausdinkite rezultatą,
#kad failas buvo sėkmingai ištrintas.
    
