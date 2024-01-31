---DB modelis: parduotuvė:
---* product (id, name, price)
---* customer (id, first_name, last_name)
---* bill (id, purchase_datetime, cashier_id, customer_id)
---* bill_line (id, bill_id, product_id, quantity)
---Užklausos:
---* daugiausiai parduodami produktai
---* didžiausia produkto apyvarta
---* geriausias klientas
---* didžiausia saskaita---


CREATE TABLE IF NOT EXISTS produktas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pavadinimas VARCHAR(50),
    kaina INTEGER
);


CREATE TABLE IF NOT EXISTS klientas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vardas VARCHAR(20),
    pavarde VARCHAR(20)
);

---DROP TABLE saskaita_faktura
CREATE TABLE IF NOT EXISTS saskaita_faktura (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pirkinio_data DATETIME,
    pardavejo_id INTEGER,
    kliento_id INTEGER REFERENCES klientas(id)
);



CREATE TABLE IF NOT EXISTS saskaitos_eilute (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fakturos_id INTEGER REFERENCES saskaita_faktura(id),
    produkto_id INTEGER REFERENCES produktas(id),
    produkto_kiekis FLOAT
);





