import socket

g = 8789678678686878
n = 994449669889999496698999
my_ip = "127.0.0.1"
porta = 2512

def main():
    global g
    global n
    client = crazione_client()
    chiave_privata = int(input("inserire il numero privato: "))
    b = int(ricevi_data(client))
    a = genera_a(g,n,chiave_privata)
    invia_data(client, a)
    chiave = genera_chiave(chiave_privata,n,b)
    messaggio = ricevi_data(client)
    decriptato = decripta_messaggio(chiave, messaggio)
    print(decriptato)

#algoritmo
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
    
#client
def ricevi_data(client):
    messaggio = client.recv(4096) 
    convertito = messaggio.decode()
    return convertito

def invia_data(client, data):
    data = str(data)
    messaggio = data.encode()
    client.sendall(messaggio)

def crazione_client():
    global my_ip
    global porta
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client.connect((my_ip,porta))
    return client

main()