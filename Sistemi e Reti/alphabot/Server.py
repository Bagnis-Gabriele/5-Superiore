"""
Server per Comandare l'Alphabot
"""

import socket
import sqlite3
import threading

my_ip = '127.0.0.1'
porta = 2512

valore_default = "non esiste"   #valore nel caso non esistano percorsi

class ClientThread(threading.Thread):
    def __init__(self,server,connessione):
        threading.Thread.__init__(self)
        self.server=server
        self.connessione=connessione
        

    def run(self):
        while(True):
            #lettura dei dati inviati dall'utente
            data = self.connessione.recv(4096)  
            richiesta = data.decode()
            #comunicazione dei dati del calcolo all'utente
            print(data)  
            percorso = elabora_Richiesta(richiesta)
            invia_dati_alphabot(self.server, self.connessione, percorso)

def crea_server():
        global my_ip
        global porta

        #creazione del socket TCP IPv4
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #bind del server per esporlo sulla rete
        server.bind((my_ip, porta))   

        #comunicazione dei dati del server all'utente
        print(f"\nIl Server è online \t {my_ip}:{porta}")

        #attesa di una connessione
        server.listen()

        return server


def connetti_alphabot(server):
    
    #accettazione delle eventuali connessioni
    connessione, _ = server.accept() 

    return connessione 

def invia_dati_alphabot(server, connessione, data):

    data= data.encode()
    #restituisco il risultato al client
    connessione.sendall(data)

def chiusura_server(server):
    #chiusura del socket
    server.close()

def elabora_Richiesta(richiesta):
    db = sqlite3.connect('percorsi.db')
    global valore_default
    cursor = db.cursor()
    try:
        inizio,fine = richiesta.split(',')
    except:
        inizio = " "
        fine = " "
    cursor.execute(f'SELECT percorso FROM (inizio_fine INNER JOIN percorsi ON (inizio_fine.id_percorso = percorsi.id) INNER JOIN luoghi s ON (id_start = s.id)) INNER JOIN luoghi f ON (id_end = f.id) WHERE "{inizio}" = s.nome AND "{fine}" = f.nome')
    percorso = cursor.fetchone()
    try:
        percorso = f"{percorso[0]}"
    except:
        percorso = valore_default
    print(percorso)
    db.close()
    return percorso

def main():
    clienti=[]
    server = crea_server()
    while(1):
        connessione = connetti_alphabot(server)
        c = ClientThread(server,connessione)
        clienti.append(c)
        c.start()

    chiusura_server(server)

if __name__ == "__main__":
    main()
