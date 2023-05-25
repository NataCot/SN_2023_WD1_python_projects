import random
secret = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess the number: "))
    attempts += 1

    if secret == guess:
        print("Congratulations!")
        print("Number of attempts: " + str(attempts))
        break
    else:
        if secret < guess:
            print("Wrong! The number you entered is too big.")
        else:
            print("Wrong! The number you entered is too small.")
