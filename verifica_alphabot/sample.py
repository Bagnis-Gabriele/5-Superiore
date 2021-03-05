def main():
    g = int(input("inserire g: "))
    n = int(input("inserire n: "))
    chiave_privata = int(input("inserire il numero privato: "))
    a = genera_a(g,n,chiave_privata)
    b = int(input("chiave ricevuta: "))
    chiave = genera_chiave(chiave_privata,n,b)
    print(chiave)
    messaggio = input ("messaggio: ")
    criptato = cripta_messaggio(chiave, messaggio)
    print (criptato)
    decriptato = decripta_messaggio(chiave, criptato)
    print(decriptato)


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
    

main()