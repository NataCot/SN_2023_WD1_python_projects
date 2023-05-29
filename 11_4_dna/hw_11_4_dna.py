with open("dna.txt") as dna_file:
    dna = dna_file.read()


def function1(characteristic):
    for x in characteristic:
        if characteristic[x] in dna:
            suspect.append(x)


def function2(person):
    if sorted(list(person.values())) == sorted(suspect):
        suspect_name = [k for k, v in people.items() if v == person]
        print("The suspect(s) are: " + str(suspect_name))


hair = {
    "black": "CCAGCAATCGC",
    "brown": "GCCAGTGCCG",
    "blonde": "TTAGCTATCGC"
}

face = {
    "square": "GCCACGG",
    "round": "ACCACAA",
    "oval": "AGGCCTCA"
}

eyes = {
    "blue": "TTGTGGTGGC",
    "green": "GGGAGGTGGC",
    "brown": "AAGTAGTGAC"
}
gender = {
    "female": "TGAAGGACCTTC",
    "male": "TGCAGGAACTTC"
}
race = {
    "white": "AAAACCTCA",
    "black": "CGACTACAG",
    "asian": "CGCGGGCCG"
}

people = {
    "eva": {
        "gender": "female",
        "race": "white",
        "hair": "blonde",
        "eyes": "blue",
        "face": "oval"
    },
    "larisa": {
        "gender": "female",
        "race": "white",
        "hair": "brown",
        "eyes": "brown",
        "face": "oval"
    },
    "matej": {
        "gender": "male",
        "race": "white",
        "hair": "brown",
        "eyes": "brown",
        "face": "oval"
    },
    "miha": {
        "gender": "male",
        "race": "white",
        "hair": "brown",
        "eyes": "green",
        "face": "square"
    }}

suspect = []

function1(hair)
function1(face)
function1(eyes)
function1(gender)
function1(race)

print("The characteristics of the suspect are: " + str(suspect))

function2(people["eva"])
function2(people["larisa"])
function2(people["matej"])
function2(people["miha"])
