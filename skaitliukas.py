import sqlite3

connector = sqlite3.connect('skaitliukas.db')
cursor = connector.cursor()

def create_table(connector: sqlite3.Connection, cursor: sqlite3.Cursor):
    query = ['''
        CREATE TABLE IF NOT EXISTS skaiciuokle (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produktas VARCHAR(20),
        kiekis INTEGER
        );
        ''',
        '''
        CREATE TABLE IF NOT EXISTS parduotuve (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pav VARCHAR(50),
        telefonas INTEGER
        );
        ''']
    for quer in query:
        cursor.execute(quer)
    connector.commit()
    
def prideti_info(connector: sqlite3.Connection, cursor: sqlite3.Cursor):
    produktas = input("Iveskite produkto pavadinima: ")
    kiekis = input('Iveskite kieki')
    with connector:
        cursor.execute("INSERT INTO skaiciuokle (produktas, kiekis)"
                       "VALUES (?, ?)", (produktas, kiekis))
    print("Info sekmingai prideta")
    
def sudetis(connector: sqlite3.Connection, cursor: sqlite3.Cursor):
    print("Kiekiu ataskaita: ")
    with connector:
        cursor.execute("SELECT kiekis FROM skaiciuokle")
        skaiciuokle = cursor.fetchall()
        if sum(kiekis[0] for kiekis in skaiciuokle) <= 0:
            print("Tuscia")
        else:
            print("yra visko", sum(kiekis[0] for kiekis in skaiciuokle))
        
            
            
def spausdinti(connector: sqlite3.Connection, cursor: sqlite3.Cursor):
    print("Ataskaita")
    with connector:
        cursor.execute("SELECT * FROM skaiciuokle")
        skaiciuokle = cursor.fetchall()
        for skaic in skaiciuokle:
            print(f"produktas: {skaic[0]}, kiekis: {skaic[1]}")
        
if __name__ == "__main__":
    create_table(connector, cursor)
           
while True:
    print("""
          1. exit
          2. Prideti info
          3. Spausdinti info
          4. Kiekiu suma
          """)
    pasirinkimas = int(input("Iveskite Jus dominanti Menu punkta: "))
    if pasirinkimas == 1:
        break
    if pasirinkimas == 2:
        prideti_info(connector, cursor)
    if pasirinkimas == 3:
        spausdinti(connector, cursor)
    if pasirinkimas == 4:
        sudetis(connector, cursor)
        


connector.close()    
                
    