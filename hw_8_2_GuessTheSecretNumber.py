import random
secret = random.randint(1, 100)
guess = input("Guess the number: ")
guess = int(guess)
if secret == guess:
    print("Congratulations!")
elif secret != guess:
    if secret < guess:
        print("Wrong! The number you entered is too big.")
    else:
        print("Wrong! The number you entered is too small.")
    print("The right number is " + str(secret))

