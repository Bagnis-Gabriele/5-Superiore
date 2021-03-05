import math

def controllo_se_primo(n):
    numeri = []
    for i in range (2, int(math.sqrt(n) + 1)):
        numeri.append(i)
    
    for num in numeri:
        if n != num and n % num == 0:
            return 0
    return 1

def trova_numero(n):
    num = 2
    cont = n
    
    while True:
        if controllo_se_primo(num):
            cont = cont -1
        if cont == 0:
            return num

        num = num + 1

def main():
    while True:
        n = input("Inserisci un numero \"exit\" per chiudere il programma: ")
        if n.lower() == "exit":
            break
        elif n.isdigit():
            print(trova_numero(int(n)))
        else:
            print("Il valore inserito non è valido")
    

if __name__ == "__main__":
    main()