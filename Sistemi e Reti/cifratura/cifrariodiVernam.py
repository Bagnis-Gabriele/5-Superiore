	
import sys,random

def cripta(Stringa, chiave,d1,d2):

    if chiave == '' or len(chiave) < len(Stringa):
            # genero la chiave
            chiave = ''
            for _ in Stringa[:-1]:
                    chiave = chiave+d2[random.randint(0,25)]

    risultato = ''
    i = 0
    while i < len(Stringa):
        if controlloCarattere(Stringa[i],d1):
            risultato = risultato+d2[abs((d1[Stringa[i]]+d1[chiave[i]])%26)]
        else:
            risultato = risultato + Stringa[i]
        i += 1

    return risultato,chiave

def controlloCarattere(c,d1):
    for e in d1:
        if(c==e):
            return True
    return False
 
def decripta(Stringa, chiave,d1,d2):

    if len(chiave)<len(Stringa):
        return "ERRORE"

    risultato = ''
    i = 0
    while i < len(Stringa):
        if controlloCarattere(Stringa[i],d1):
            risultato = risultato+d2[abs((d1[Stringa[i]]-d1[chiave[i]])%26)]
        else:
            risultato = risultato + Stringa[i]
        i += 1

    return risultato
       
 
def main():
    d1 = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
    d2 = {}

    for chiave in d1:
            d2[d1[chiave]] = chiave

    parola = input("inserire la stringa da criptare/decriptare\n\t")
    parola = parola.lower()
    chiave = input("inserire la chiave\n\t")
    chiave = chiave.lower()

    modalita='a'
    while(not(modalita=='c' or modalita=='d')):
        modalita = input("inserire la modalità: \n\t c - cripta \n\t d - decripta\n\n\t")
    
    risultato = ""
    if modalita == 'c':
        risultato,chiave = cripta(parola,chiave,d1,d2)

    elif modalita == 'd':
        risultato = decripta(parola,chiave,d1,d2)

    print(f"la stringa ottenuta è: \n{risultato}\nLa chiave è: \n{chiave}")

if __name__ == "__main__":
    main()