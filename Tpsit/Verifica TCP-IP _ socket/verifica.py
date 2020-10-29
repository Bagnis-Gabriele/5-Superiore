"""
Scansione porte TCP 
"""
import socket

#parametri dell'attacco
ip = '127.0.0.127'    #IP DELL'HOST DA ATTACCARE
porta_min = 0
porta_max = 1000

#lista per memorizzare le porte disponibili
connessioni_riuscite = []

#variabile che indica la porta che sto attaccando
porta= porta_min

while (porta<porta_max):
    #stampo dati del tentativo
    print(f"\nprova a connettermi alla porta {porta}")
    #creazione del socket client TCP IPv4
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    #tentativo di connessione alla porta selezionata
    riuscita = client.connect_ex((ip,porta))
    #salvataggio delle porte funzionanti
    if (riuscita==0):
        connessioni_riuscite.append(porta)
        print("\n\tconnessione riuscita")
    else:
        print("\n\tconnessione fallita")
    #chiusura del socket 
    client.close()
    #aggiornamento - passo alla porta successiva
    porta += 1

print ("porte su cui è riuscita la connessione:")
print (connessioni_riuscite)


