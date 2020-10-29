import threading
import socket


class ClientThread(threading.Thread):
    def __init__(self,conn,indirizzo):
        threading.Thread.__init__(self)
        self.indirizzo_client = indirizzo
        self.connessione = conn
        self.vivo = 0

    def run(self):
        while(True):
            try:
                #lettura dei dati inviati dall'utente
                data = self.connessione.recv(4096)  

                #comunicazione dei dati del calcolo all'utente
                print(str(self.indirizzo_client) + ": \t" + data.decode())

                #restituisco il risultato al client
                self.connessione.sendall(data)
            except:
                if (self.vivo == 0):
                    self.vivo = 1
                    print (f"il cliente {self.indirizzo_client} si è disconnesso")
                else:
                    pass

def main():
    clienti = []
    ip = '192.168.88.106'
    porta = 6000

    #creazione del socket TCP IPv4
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #bind del server per esporlo sulla rete
    server.bind((ip, porta))   

    #comunicazione dei dati del server all'utente
    print(f"\nIl Server è online \t {ip}:{porta}")

    #attesa di una connessione
    server.listen()

    while (True):
        #accettazione delle eventuali connessioni
        connessione, porta = server.accept()
        c= ClientThread(connessione,porta)
        clienti.append(c)
        print (f"il cliente {c.indirizzo_client} si è connesso")
        clienti[-1].start()

if __name__ == "__main__":
    main()