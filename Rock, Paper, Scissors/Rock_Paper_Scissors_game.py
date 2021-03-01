import random
#Juego de roca, papel y tijeras
mano=["roca","papel","tijeras"]
def main():
    maquina = (random.choice(mano))

    print("Bienvenido al juegos de piedra, papel y tijeras porfavor ingresa tu eleccion")
    jugador = str(input("Jugador selecciona:"))
    print("maquina selecciona:"+maquina)

    if jugador == maquina :   
        print("Empate")
    elif jugador == "roca" and maquina == "tijeras":
        print("Ganaste")
    elif jugador == "papel" and maquina == "roca":
        print("Ganaste")
    elif jugador == "tijeras" and maquina == "papel":
        print("Ganaste")
    elif jugador == "roca" and maquina == "papel":
        print("Perdiste")
    elif jugador == "papel" and maquina == "tijeras":
        print("Perdiste")
    elif jugador == "tijeras" and maquina == "roca" :
        print("Perdiste")

    main()

main()