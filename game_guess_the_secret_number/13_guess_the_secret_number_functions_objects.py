import random
import json
import datetime


class Result:
    def __init__(self, attempts, date, name):
        self.attempts = attempts
        self.date = date
        self.name = name


def score(file):
    with open(file) as score_file:
        score_list = json.loads(score_file.read())
        score_list.sort(key=lambda x: x["attempts"])
        return score_list


def top_scores(ts):
    print("Top three best scores: ")
    try:
        print(
            f'{chr(0x20) * 10}'
            f'{ts[0]["attempts"]}'
            f'{chr(0x20) * 10}'
            f'{ts[1]["attempts"]}'
            f'{chr(0x20) * 10}'
            f'{ts[2]["attempts"]}')
    except IndexError:
        print("%s Insufficient data to expose." % (' ' * 5))


def game_guessed(score, file):
    date = datetime.datetime.now()
    result_obj = Result(attempts=attempt, date=date.strftime("%m/%d/%Y, %H:%M:%S"), name=name)
    score.append(result_obj.__dict__)

    with open(file, "w+") as score_file:
        score_file.write(json.dumps(score))

    print("Congratulations! You guessed the number.")
    print("Number of attempts: " + str(attempt))


secret = random.randint(1, 50)

print("Welcome to the game 'Guess the secret number'!")

name = input("Please enter your name: ")

while True:
    level = input("Please choose a level: e for easy, m for medium or h for hard ")
    attempt = 0
    if level == "e":
        score_easy = score(file="score_easy.json")
        top_scores(ts=score_easy)

        while True:
            guess = input("Please enter a number in range of 1 and 50: ")
            attempt += 1
            try:
                guess = float(guess)
            except ValueError:
                print("Only numbers allowed. Please try again.")
            else:
                if guess == secret:
                    game_guessed(score=score_easy, file="score_easy.json")
                    question = input("Write 'continue' to play again, 'score' to view scores or press any button to end the game ")
                    if question == "continue":
                        continue
                    elif question == "score":
                        score_easy = score(file="score_easy.json")
                        print(score_easy)
                        question2 = input("Write 'continue' or press any button to end the game ")
                        if question2 == "continue":
                            continue
                        else:
                            print("Game over!")
                            break
                    else:
                        print("Game over!")
                        break
                elif guess in range((secret - 3), (secret + 3)):
                    print("Almost, but not quite. Please try again.")
                elif guess < (secret + 3):
                    print("The number you entered is too small. Please try again.")
                else:
                    print("The number you entered is too big! Please try again.")
        break
    elif level == "m":
        score_medium = score(file="score_medium.json")
        top_scores(ts=score_medium)
        while True:
            guess = input("Please enter a number: ")
            attempt += 1
            try:
                guess = float(guess)
            except ValueError:
                print("Only numbers allowed. Please try again.")
            else:
                if guess == secret:
                    game_guessed(score=score_medium, file="score_medium.json")
                    question = input("Write 'continue' to play again, 'score' to view scores or press any button to end the game ")
                    if question == "continue":
                        continue
                    elif question == "score":
                        score_medium = score(file="score_medium.json")
                        print(score_medium)
                        question2 = input("Write 'continue' or press any button to end the game ")
                        if question2 == "continue":
                            continue
                        else:
                            print("Game over!")
                            break
                    else:
                        print("Game over!")
                        break
                elif guess < secret:
                    print("The number you entered is too small. Please try again.")
                else:
                    print("The number you entered is too big. Please try again.")
        break
    elif level == "h":
        score_hard = score(file="score_hard.json")
        top_scores(ts=score_hard)
        while True:
            guess = input("Please enter a number: ")
            attempt += 1
            try:
                guess = float(guess)
            except ValueError:
                print("Only numbers allowed. Please try again.")
            else:
                if guess == secret:
                    game_guessed(score=score_hard, file="score_hard.json")
                    question = input("Write 'continue' to play again, 'score' to view scores or press any button to end the game ")
                    if question == "continue":
                        continue
                    elif question == "score":
                        score_hard = score(file="score_hard.json")
                        print(score_hard)
                        question2 = input("Write 'continue' or press any button to end the game ")
                        if question2 == "continue":
                            continue
                        else:
                            print("Game over!")
                            break
                    else:
                        print("Game over!")
                        break
                else:
                    print("Please try again")
        break
    else:
        continue
