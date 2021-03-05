"""
socket tcp 
send per inviare la post (guardare da appunti, come stringa in python)
"""

"""
Client ECHO UDP 
"""
import socket


ip_server = '127.0.0.1'
porta_server = 5000

#creazione del socket TCP IPv4
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

#connessione al server
client.connect((ip_server,porta_server))


#richiesta del messaggio
password = "gabrieles"
username = "bagnis"

body= f"username={username}&password={password}"
body_lenght= len(body)

request= f"POST http://127.0.0.1:5000/ HTTP/1.1\nHost: http://127.0.0.1:5000\nContent-Type:application/x-www-form-urlencoded\nContent-Length: {body_lenght}\n\n{body}"

#invio dei dati al server
client.sendall(request.encode())

#leggo il risultato
risultato = client.recv(4096)

#controllo se il server è connesso
print ("connessione: " + risultato.decode())

risultato = client.recv(4096)
risultato = risultato.decode()

#comunicazione risultato all'utente
if ("redirect" in risultato):
    print("login eseguito")
else:
    print("login fallito")

#chiusura del socket
client.close()