import random
num = random.randrange(1,50)
def main():
    print("Bienvenido al juego adivina el numero del 1 al 50")
    numero = int(input("ingresa el numero"))

    while numero != num:
        if numero< num:
            print("el numero es mas alto. intenta de nuevo")
            numero = int(input("ingresa el numero"))
        else:
            print("el numero es menor. intenta de nuevo")
            numero = int(input("ingresa el numero"))

    print("felicidades acertaste!")
    main()

main()