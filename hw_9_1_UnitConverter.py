print("Greetings! This program will help you convert kilometers into miles and viceversa.")

while True:
    x = input("Enter the number: ")
    x1 = float(x.replace(",", "."))
    y = input("Enter the unit: ")
    km = float(x1 / 0.621271)
    mi = float(x1 * 0.621271)

    if y == "km":
        print(str(x1) + " km is " + str(mi) + " miles.")
    else:
        print(str(x1) + " mi is " + str(km) + " kilometers.")

    z = input("Do you want to make another conversion? Yes or no answer ")
    if z == "no":
        print("Thank you for using this unit converter. Have a nice day!")
        break
