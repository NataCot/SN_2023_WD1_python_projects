number1 = input("Choose your number 1: ")
number1 = int(number1)
number2 = input("Choose your number 2: ")
number2 = int(number2)
arithmeticOperation = input("Choose an arithmetic operation +, -, * or /: ")

if arithmeticOperation == "+":
    print(number1 + number2)
elif arithmeticOperation == "-":
    print(number1 - number2)
elif arithmeticOperation == "*":
    print(number1 * number2)
else:
    print(number1 / number2)
