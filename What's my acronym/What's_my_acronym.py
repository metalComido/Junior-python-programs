
def acronym(phrase):
    a = ""
    for words in phrase.split():
        a = a + words[0]
    return a

def main():
    print("insert a full meaning of organization or concepto to get is acronym")
    text = input("Please enter your phrase: ")
    text = text.upper()

    answer = acronym(text)

    print(str(answer))
main()