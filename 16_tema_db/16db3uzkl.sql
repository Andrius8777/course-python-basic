--Sukurkite duomenų bazę, kurioje saugosite informaciją apie studentų duomenis ir
-- jų kursus. Kiekvienas studentas gali mokytis daugelyje kursų, ir kiekvienas kursas
-- gali turėti daug studentų. Sukurkite atitinkamas lentelės ir susiekite jas
-- Many-to-Many ryšiu

CREATE TABLE studentai (
id INTEGER PRIMARY KEY AUTOINCREMENT,
    vardas VARCHAR(50) NOT NULL,
    pavarde VARCHAR(50) NOT NULL
);


--DROP TABLE studentai;
INSERT INTO studentai (vardas, pavarde)
VALUES("SAULIUS", "BALVONAS");
INSERT INTO studentai (vardas, pavarde)
VALUES("JUOZAS", "MAZAS");
INSERT INTO studentai (vardas, pavarde)
VALUES("JURGA", "SPURGA");

CREATE TABLE kursai (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kursu_pav VARCHAR(100) NOT NULL
);

INSERT INTO kursai (kursu_pav)
VALUES("MATEMATIKA");
INSERT INTO kursai (kursu_pav)
VALUES("DAILE");
INSERT INTO kursai (kursu_pav)
VALUES("FIZIKA");


CREATE TABLE st_kursai (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    st_id INTEGER REFERENCES studentai(id),
    kurso_id INTEGER REFERENCES kursai(id)
);

SELECT vardas, kursu_pav FROM st_kursai
    JOIN 





