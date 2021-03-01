print("bienvenido al juego para crear una historia")

def main():
    print ("ingresa los datos que se te piden para completar la historia")
    name = input("algun nombre: ")
    animo = input("cual es tu estado de animo: ")
    lugar = input("ingresa el nombre de algun lugar: ")
    adjetivo = input("ingresa un adjetivo: ")
    despido = input("ingresa una frase de despedida: ")

    print("hola, como estas cual es tu nombre? ",name)
    print("como te encuentras? ",animo ,"oye sabes que te encuentras en ",lugar)
    print("no crees que este lugar es muy ",adjetivo)
    print("me debo de ir que te vaya bien, ",despido    )
    main()

main()

