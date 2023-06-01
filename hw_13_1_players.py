class BasketballPlayers:
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

    def weight_ibs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds

    def height_inch(self):
        inches = self.height_cm * 0.393700787
        return inches


lebron = BasketballPlayers(
    first_name="James",
    last_name="Lebron",
    height_cm=203,
    weight_kg=113,
    points=27.2,
    rebounds=7.4,
    assists=7.2
)
KD = BasketballPlayers(
    first_name="Kevin",
    last_name="Durant",
    height_cm=210,
    weight_kg=108,
    points=27.2,
    rebounds=7.1,
    assists=4
)
MJ = BasketballPlayers(
    first_name="Michael",
    last_name="Jordan",
    height_cm=198,
    weight_kg=98,
    points=32.292,
    rebounds=6.2,
    assists=5.3
)

print(lebron.first_name)


class FootballPlayers():
    def __int__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


ronaldo = FootballPlayers(
    first_name="Cristiano",
    last_name="Ronaldo",
    height_cm=184,
    weight_kg=79,
    goals=586,
    yellow_cards=95,
    red_cards=11
)
messi = FootballPlayers(
    first_name="Lionel",
    last_name="Messi",
    height_cm=170,
    weight_kg=67,
    goals=575,
    yellow_cards=67,
    red_cards=0
)

print(ronaldo.first_name)
