print("Welcome to FizzBuzz!")
x = int(input("Please select a whole number between 1 and 100: "))

for x in range(1, x + 1):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
print("The End!")
