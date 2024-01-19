import mano_mod #pagrindiniam faile pagrindinis.py importuojam info is mano_mod.py
from mano_mod import ManoKlase
from math import *


print(mano_mod.pasisveikinti('Andrius')) # Sveikas, Andrius!
print(mano_mod.sudetis(10, 5)) # 15 PAEME IS FUNKCIJOS DEF SUDETIS

#jei is klases tai reikia importuotis klase: "from mano_mod import ManoKlase"

atsakymas = ManoKlase(5)
print(atsakymas)   # issiaiskint  <mano_mod.ManoKlase object at 0x000001AC7929A870>

