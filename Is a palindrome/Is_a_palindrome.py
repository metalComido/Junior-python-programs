
print("Bienvenido, ingresa una palabra para saber si es palindromo")
def main():
    palabra = input("ingresa la palabra: ")
    l = len(palabra)
    p = l-1
    index = 0
    while index < p:
        if palabra[index] == palabra[p]:
            index = index + 1
            p = p-1
            if index == p or index + 1 == p:
                print("la palabra es palindromo")
        else:
            print("la palabra no es palindromo")
            break
    main()

main()