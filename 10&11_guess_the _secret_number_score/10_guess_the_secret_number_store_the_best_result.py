import random

print("Welcome to 'Guess The Secret number' game!")

secret = random.randint(1, 25)

attempts = 0

with open("best_score.txt") as best_score_file:
    total = best_score_file.read()
    num1, num2, num3 = total.split()
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    print("The first three best scores are: " + str(total))

while True:
    guess = input("Enter a number in range from 1 to 25: ")
    attempts = attempts + 1
    try:
        guess = float(guess)
    except ValueError:
        print("Only numbers are allowed. Please try again.")
    else:
        if guess < 1 or guess > 25:
            print("Only the numbers between 1 and 25 are allowed. Please try again.")
        elif guess > secret:
            print("The number you have choose is to big. Please try again.")
        elif guess < secret:
            print("The number you have choose is to small. Please try again.")
        else:
            print("Congratulations! You won the game in " + str(attempts) + " attempts!")
            if attempts < num1:
                with open("best_score.txt", "w") as best_score_file:
                    best_score_file.write(str(attempts) + " ")
                    best_score_file.write(str(num1) + " ")
                    best_score_file.write(str(num2) + " ")
            elif attempts < num2:
                with open("best_score.txt", "w") as best_score_file:
                    best_score_file.write(str(num1) + " ")
                    best_score_file.write(str(attempts) + " ")
                    best_score_file.write(str(num2) + " ")
            elif attempts < num3:
                with open("best_score.txt", "w") as best_score_file:
                    best_score_file.write(str(num1) + " ")
                    best_score_file.write(str(num2) + " ")
                    best_score_file.write(str(attempts) + " ")
            else:
                with open("best_score.txt", "w") as best_score_file:
                    best_score_file.write(str(num1) + " ")
                    best_score_file.write(str(num2) + " ")
                    best_score_file.write(str(num3) + " ")
            break
