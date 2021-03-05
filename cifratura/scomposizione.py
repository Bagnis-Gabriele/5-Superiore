import math

def controllo_se_primo(n):
    numeri = []
    for i in range (2, int(math.sqrt(n) + 1)):
        numeri.append(i)
    
    for num in numeri:
        if n != num and n % num == 0:
            return 0
    return 1

def fattorizza(n):
    if controllo_se_primo(n):
        print("numero primo")
        return [n]

    fattori = []  
    num_analizzato = n

    for i in range(2,int(n/2)+1):
        cond = 1
        while cond:
            if (num_analizzato % i) == 0:
                fattori.append(i)
                num_analizzato = num_analizzato / i
            else:
                cond = 0
    return fattori

def main():
    while True:
        n = input("Inserisci un numero \"exit\" per chiudere il programma: ")
        if n.lower() == "exit":
            break
        elif n.isdigit():
            print(fattorizza(int(n)))
        else:
            print("Il valore inserito non è valido")

if __name__ == "__main__":
    main()