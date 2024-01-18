from zmogus import Zmogus
import pickle
import os

ZMONES_FILE = 'PTU20_live/zmones.pkl'

if os.path.exists(ZMONES_FILE):
    with open(ZMONES_FILE, "rb") as zmones_file:
        zmones = pickle.load(zmones_file)
        
print('\n\n---[ Visi zmones ]---')
for zmogus in zmones:
    print(zmogus.vardas, zmogus.amzius)
