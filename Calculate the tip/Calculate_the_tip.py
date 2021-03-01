
def main():
    print("cuál es la factura total de hoy, por favor?")
    money = float(input())
    tip = money * 00.18
    count = money + tip
    print("18% propiena es $",round(tip), "lo que lleva tu total a",round(count))
    main()
main()