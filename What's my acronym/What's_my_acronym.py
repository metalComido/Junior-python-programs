
def acronym(phrase):
    a = ""
    for words in phrase.split():
        a = a + words[0]
    return a

def main():
    print("inserte un significado completo de organización o concepto para obtener es el acrónimo")
    text = input("Por favor ingrese su organización: ")
    text = text.upper()

    answer = acronym(text)

    print(str(answer))
main()