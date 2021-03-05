import socket

g = 8789678678686878
n = 994449669889999496698999
my_ip = "127.0.0.1"
porta = 2512

def main():
    global g
    global n
    server = crea_server()
    connessione = connetti_client(server)
    chiave_privata = int(input("inserire il numero privato: "))
    a = genera_a(g,n,chiave_privata)
    invia_dati_client(connessione, a)
    b = int(ricevi_dati_client(connessione))
    chiave = genera_chiave(chiave_privata,n,b)
    messaggio = input ("messaggio: ")
    criptato = cripta_messaggio(chiave, messaggio)
    invia_dati_client(connessione, criptato)

# algoritmo
def genera_a(g,n,chiave_privata):
    a = g**chiave_privata
    a = a%n
    return a

def genera_chiave(chiave_privata,n,b):
    chiave = b**chiave_privata
    chiave = chiave%n
    return chiave
    
def cripta_messaggio(chiave, messaggio):
    messaggio_criptato = ""
    for c in messaggio:
        messaggio_criptato += chr(ord(c)+chiave)
    return messaggio_criptato

def decripta_messaggio(chiave, messaggio_criptato):
    messaggio_decriptato = ""
    for c in messaggio_criptato:
        messaggio_decriptato += chr(ord(c)-chiave)
    return messaggio_decriptato

#server
def crea_server():
    global my_ip
    global porta

    #creazione del socket TCP IPv4
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #bind del server per esporlo sulla rete
    server.bind((my_ip, porta))   

    #comunicazione dei dati del server all'utente
    print (f"\nIl server è online:  \t {my_ip}:{porta}")

    #attesa di una connessione
    server.listen()

    return server

def ricevi_dati_client(connessione):
    #ricevo una stringa dal client
    risultato = connessione.recv(4096) 
    risultato = risultato.decode()
    return risultato

def connetti_client(server):
    #accettazione delle eventuali connessioni
    connessione, _ = server.accept() 
    return connessione 

def invia_dati_client(connessione, data):
    data = str(data)
    data= data.encode()
    #restituisco il risultato al client
    connessione.sendall(data)

def chiusura_server(server):
    #chiusura del socket
    server.close()
    

main()