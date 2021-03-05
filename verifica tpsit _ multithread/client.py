"""
Client ECHO UDP 
"""
import socket
import logging

ip_server = '127.0.0.1'
porta_server = 2512

logging.basicConfig(level = logging.DEBUG, filename="logging_client.log", filemode="a")
logger = logging.getLogger()

#creazione del socket TCP IPv4
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

#connessione al server
client.connect((ip_server,porta_server))

logger.info("connesso al server")

while(True):
    #leggo il messaggio
    messaggio = client.recv(4096) 

    operazione = messaggio.decode()

    if (operazione)=="exit":
        logger.info("chiusura client")
        break

    try:
        risultato = str(eval(operazione))
    except:
        risultato = "error"
    
    logging.info(f"{operazione} = {risultato}")
    data = risultato.encode()

    #invio dei dati al server
    client.sendall(data)

#chiusura del socket
client.close()

