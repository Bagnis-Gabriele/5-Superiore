def euclide(a,b):
    if b > a:
        a , b = b , a

    while True:
        val = a % b
        if val == 0:
            return b
        else:
            a = b
            b = val

def main():
    a = int(input("Inserisci il primo numero: "))
    b = int(input("Inserisci il secondo numero: "))
    print(euclide(a,b))
    

if __name__ == "__main__":
    main()