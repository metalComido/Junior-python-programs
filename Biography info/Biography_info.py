
def main():
    Name = str(input("Whats is you name: "))
    print("Add you birthday")
    day , month , year = int(input("day:")) , str(input("month:")), int(input("year:"))
    print("Add your adress")
    adress,city = str(input("Adress: ")),str(input("city: "))
    goal= str(input("add yout personal goal:"))

    print("- Name: {}".format(Name))
    print("- Date of birth: {} {},{}".format(month, day, year))
    print("- Address: {}, {}".format(adress,city))
    print("- Personal goals: {}".format(goal))
    main()

main()