"""
Server FILE TCP 
"""
import socket

ip = '192.168.43.202'    #IL MIO IP
porta = 7000

"""
CREATE SOCKET
"""
#creazione del socket TCP IPv4
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind del server per esporlo sulla rete
server.bind((ip, porta))   

#comunicazione dei dati del server all'utente
print(f"\nIl Server è online \t {ip}:{porta}")

"""
SERVER
"""
#attesa di una connessione
server.listen()

#accettazione delle eventuali connessioni
connessione, indirizzo_client = server.accept()

#lettura dei dati inviati dall'utente
title = connessione.recv(4096)  
data = connessione.recv(4096) 

#creazione file
file1 = open("image.png","w")
file1.write(data.decode())
file1.close()

print ("file create")

#chiusura del socket
server.close()
