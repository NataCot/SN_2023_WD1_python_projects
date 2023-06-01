import random

countries_cities = {
    "Austria": "Vienna",
    "Belgium": "Brussels",
    "Bulgaria": "Sofia",
    "Croatia": "Zagreb",
    "Republic of Cyprus": "Nicosia",
    "Czech Republic": "Prague",
    "Denmark": "Copenhagen",
    "Estonia": "Tallinn",
    "Finland": "Helsinki",
    "France": "Paris",
    "Germany": "Berlin",
    "Greece": "Athens",
    "Hungary": "Budapest",
    "Ireland": "Dublin",
    "Italy": "Rome",
    "Latvia": "Riga",
    "Lithuania": "Vilnius",
    "Luxembourg": "Luxembourg",
    "Malta": "Valletta",
    "Netherlands": "Amsterdam",
    "Poland": "Warsaw",
    "Portugal": "Lisbon",
    "Romania": "Bucharest",
    "Slovakia": "Bratislava",
    "Slovenia": "Ljubljana",
    "Spain": "Madrid",
    "Sweden": "Stockholm"
}

print("Welcome to the game 'Geography quiz")
print("Please answer the questions:")
correct_result = 0
attempts = 0
while len(countries_cities) != 0:
    country, city = random.choice(list(countries_cities.items()))
    countries_cities.pop(country)
    game = input("What is the capital city of " + str(country) + "? ")
    if game == city:
        print("Correct!")
        correct_result += 1
    else:
        print("Wrong!")
    attempts += 1

result = format(correct_result/attempts, ".2f")
print("You answered correctly " + str(result) + "% of the answers")
