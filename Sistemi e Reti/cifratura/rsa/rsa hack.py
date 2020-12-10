import math

def controllo_se_primo(num):
    numeri = []
    for i in range (2, int(math.sqrt(num) + 1)):
        numeri.append(i)
    
    for n in numeri:
        if num != n and num % n == 0:
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
    n = int(input("inserire n : "))
    print (fattorizza (n))
    



main()