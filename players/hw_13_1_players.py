class Players:
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_ibs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds

    def height_inch(self):
        inches = self.height_cm * 0.393700787
        return inches


class BasketballPlayers(Players):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


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


class FootballPlayers(Players):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


ronaldo = FootballPlayers(
    first_name="Cristiano",
    last_name="Ronaldo",
    height_cm=184,
    weight_kg=79,
    goals=495,
    yellow_cards=84,
    red_cards=8
)
messi = FootballPlayers(
    first_name="Lionel",
    last_name="Messi",
    height_cm=170,
    weight_kg=67,
    goals=496,
    yellow_cards=50,
    red_cards=0
)
neymar = FootballPlayers(
    first_name="Neymar",
    last_name="da Silva Santos",
    height_cm=175,
    weight_kg=68,
    goals=150,
    yellow_cards=59,
    red_cards=6
)


def new_players(sport):
    with open(sport, "a+") as file:
        file.write(str(new_player.__dict__) + "\n")


print("Fill in new player's data:")

f_name = input("Enter player's first name: ")
l_name = input("Enter player's last name: ")
height = input("Enter player's height in cm: ")
weight = input("Enter player's weight in kg: ")

sport = input("Enter a sport: ")
if sport == "football":
    goals = input("Enter the number of player's goals: ")
    yellow_cards = input("Enter the number of player's yellow cards: ")
    red_cards = input("Enter the number of player's red cards: ")
    new_player = FootballPlayers(
        first_name=f_name,
        last_name=l_name,
        height_cm=float(height),
        weight_kg=float(weight),
        goals=float(goals),
        yellow_cards=float(yellow_cards),
        red_cards=float(red_cards)
    )
    new_players("football_players.json")
    print("Player successfully entered!")
    print("Player's data: {0}".format(new_player.__dict__))
elif sport == "basketball":
    points = input("Enter the number of points: ")
    rebounds = input("Enter the number of rebounds: ")
    assists = input("Enter the number of assists: ")
    new_player = BasketballPlayers(
        first_name=f_name,
        last_name=l_name,
        height_cm=float(height),
        weight_kg=float(weight),
        points=float(points),
        rebounds=float(rebounds),
        assists=float(assists)
    )
    new_players("basketball_players.json")
    print("Player successfully entered!")
    print("Player's data: {0}".format(new_player.__dict__))
else:
    print("Not available")



