
import random
import json
import datetime

current_time = datetime.datetime.now()

secret = random.randint(1, 25)
attempt = 0
print("Welcome to the game 'Guess the secret number'")
print(current_time)

with open("score_list.json") as score_file:
    score_list = json.loads(score_file.read())
    score_list.sort(key=lambda x: x["attempts"])

print("Top scores: " + str(score_list[0]["attempts"]) + ", " + str(score_list[1]["attempts"]) + ", " + str(score_list[2]["attempts"]))

while True:
    guess = int(input("Please enter a number: "))
    attempt += 1

    if guess == secret:
        score_list.append({"attempts": attempt, "date": str(datetime.datetime.now())})

        with open("score_list.json", "w+") as score_file:
            score_file.write(json.dumps(score_list))

        print("Congratulations! You guessed the number.")
        print("Number of attempts: " + str(attempt))
        break
    elif guess < secret:
        print("The number you entered is too small! Please try again.")
    else:
        print("The number you entered is too big! Please try again")
