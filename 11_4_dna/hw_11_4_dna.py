with open("dna.txt") as dna_file:
    dna = dna_file.read()


def function1(characteristic):
    for x in characteristic:
        if characteristic[x] in dna:
            suspect.append(x)


def function2(person):
    if list(person.values()) == suspect:
        print(person)


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

eva = {
    "gender": "female",
    "race": "white",
    "hair": "blonde",
    "eyes": "blue",
    "face": "oval"
}

larisa = {
    "gender": "female",
    "race": "white",
    "hair": "brown",
    "eyes": "brown",
    "face": "oval"
}

matej = {
    "gender": "male",
    "race": "white",
    "hair": "brown",
    "eyes": "brown",
    "face": "oval"
}

miha = {
    "gender": "male",
    "race": "white",
    "hair": "brown",
    "eyes": "green",
    "face": "square"
}

suspect = []

function1(hair)
function1(face)
function1(eyes)
function1(gender)
function1(race)

# suspect.sort()
print(suspect)

function2(eva)
function2(larisa)
function2(matej)
function2(miha)
