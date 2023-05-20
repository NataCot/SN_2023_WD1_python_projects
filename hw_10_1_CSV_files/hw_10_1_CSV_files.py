# f = open("csvfile.csv", "x")

with open("csvfile.csv") as csvfile:
    rows = csvfile.read().split("\n")
    for items in rows:
        item = items.split(",")
        print(item[0] + " is " + item[1] + " years old and " + item[2] + ".")
