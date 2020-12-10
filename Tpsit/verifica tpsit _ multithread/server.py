]"""
Server per Comandare l'Alphabot
"""

import socket
import sqlite3
import threading
import logging

my_ip = '127.0.0.1'
porta = 2512

logging.basicConfig(level = logging.DEBUG, filename="logging_server.log", filemode="a")
logger = logging.getLogger()

class ClientThread(threading.Thread):
    def __init__(self,server,connessione,n,database,client):
        threading.Thread.__init__(self)
        self.server = server
        self.connessione = connessione
        self.num = n
        self.database = database
        self.client = client

    def run(self):
        for key, data in self.database.items():
            if(key == self.num):
                for operazione in data:
                    invia_dati_client(self.connessione, str(operazione))
                    risultato = ricevi_dati_client(self.connessione)
                    if(risultato != "error"):
                        print (f"{operazione} = {risultato} from {self.client[0]} - {self.client[1]}")
                        logger.info(f"{operazione} = {risultato} from {self.client[0]} - {self.client[1]}")
                    else:
                        print (f"{operazione} = ERROR from {self.client[0]} - {self.client[1]}")
                        logger.info(f"{operazione} = ERROR from {self.client[0]} - {self.client[1]}")
        invia_dati_client(self.connessione, "exit")
        logger.info(f"disconnessione client {self.num}")
                
def crea_server():
    global my_ip
    global porta

    #creazione del socket TCP IPv4
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #bind del server per esporlo sulla rete
    server.bind((my_ip, porta))   

    #comunicazione dei dati del server all'utente
    logger.info(f"\nIl server è online:  \t {my_ip}:{porta}")

    #attesa di una connessione
    server.listen()

    return server

def ricevi_dati_client(connessione):
    #ricevo una stringa dal client
    risultato = connessione.recv(4096) 
    risultato = risultato.decode()
    return risultato

def connetti_client(server):
    try:
        #accettazione delle eventuali connessioni
        connessione, client = server.accept() 
    except: 
        connessione = None
        logger.error("4.1, errore nella creazione della connessione")
    return connessione, client 

def invia_dati_client(connessione, data):
    try:
        data= data.encode()
        #restituisco il risultato al client
        connessione.sendall(data)
    except:
        logger.error("3.1, connessione persa")

def chiusura_server(server):
    #chiusura del socket
    server.close()
    logger.info(f"Il server è stato chiuso")

def caricaDatabase():
    database = {}
    try:
        db = sqlite3.connect('operations.db')
        cursor = db.cursor()
    except:
        logger.error("4.1, database inesistente")
        return [0]
    try:
        cursor.execute('SELECT client, operation FROM operations')
        data = cursor.fetchall()
    except:
        logger.error("4.1, errore nell'eseguizione della query")
    
    for element in data:
        database[element[0]]=[]
        
    for element in data:
        database[element[0]].append(element[1])

    logger.info("Database caricato")
    db.close()
    return database

def main():
    clienti=[]
    server = crea_server()
    database = caricaDatabase()
    n = 1
    while(1):
        connessione, client = connetti_client(server)
        c = ClientThread(server,connessione,n,database,client)
        clienti.append(c)
        c.start()
        n = n+1

    chiusura_server(server)

if __name__ == "__main__":
    main()
