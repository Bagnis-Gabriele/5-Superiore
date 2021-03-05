import sqlite3

#crea un dizionario che contiene i dati di tutti i percorsi
def read_all(): 
    with sqlite3.connect('static/percorsi.db') as con:
        cur = con.cursor()
        cur.execute("SELECT l1.nome, l2.nome, percorsi.percorso, percorsi.id FROM ((inizio_fine p INNER JOIN luoghi l1 ON (p.id_start=l1.id)) INNER JOIN luoghi l2 ON (p.id_end=l2.id)) INNER JOIN percorsi ON (p.id_percorso = percorsi.id)")
        rows = cur.fetchall()
        percorsi = []
        for row in rows:
            riga = {}
            riga["inizio"] = row[0]
            riga["fine"] = row[1]
            riga["percorso"] = row [2]
            riga["id"] = row [3]
            percorsi.append(riga)
    return percorsi

#crea un dizionario che contiene i dati di tutti i percorsi
def search_by_id(id): 
    with sqlite3.connect('static/percorsi.db') as con:
        cur = con.cursor()
        cur.execute("SELECT l1.nome, l2.nome, percorsi.percorso, percorsi.id FROM ((inizio_fine p INNER JOIN luoghi l1 ON (p.id_start=l1.id)) INNER JOIN luoghi l2 ON (p.id_end=l2.id)) INNER JOIN percorsi ON (p.id_percorso = percorsi.id)")
        rows = cur.fetchall()
        percorsi = []
        for row in rows:
            if(row[3]==id):
                riga = {}
                riga["inizio"] = row[0]
                riga["fine"] = row[1]
                riga["percorso"] = row [2]
                riga["id"] = row [3]
                percorsi.append(riga)
    return percorsi

def search_by_place(place): 
    with sqlite3.connect('static/percorsi.db') as con:
        cur = con.cursor()
        cur.execute("SELECT l1.nome, l2.nome, percorsi.percorso, percorsi.id FROM ((inizio_fine p INNER JOIN luoghi l1 ON (p.id_start=l1.id)) INNER JOIN luoghi l2 ON (p.id_end=l2.id)) INNER JOIN percorsi ON (p.id_percorso = percorsi.id)")
        rows = cur.fetchall()
        percorsi = []
        for row in rows:
            if(row[0]==place or row[1]==place):
                riga = {}
                riga["inizio"] = row[0]
                riga["fine"] = row[1]
                riga["percorso"] = row [2]
                riga["id"] = row [3]
                percorsi.append(riga)
    return percorsi

def search_route(start,end): 
    with sqlite3.connect('static/percorsi.db') as con:
        cur = con.cursor()
        cur.execute("SELECT l1.nome, l2.nome, percorsi.percorso, percorsi.id FROM ((inizio_fine p INNER JOIN luoghi l1 ON (p.id_start=l1.id)) INNER JOIN luoghi l2 ON (p.id_end=l2.id)) INNER JOIN percorsi ON (p.id_percorso = percorsi.id)")
        rows = cur.fetchall()
        percorsi = []
        for row in rows:
            if(row[0]==start and row[1]==end):
                riga = {}
                riga["inizio"] = row[0]
                riga["fine"] = row[1]
                riga["percorso"] = row [2]
                riga["id"] = row [3]
                percorsi.append(riga)
    return percorsi