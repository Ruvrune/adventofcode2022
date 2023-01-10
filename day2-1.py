
# with open("adventofcode22/input2-1.txt") as text_file:
#     list_of_food = []
#     summed_list_of_food = []
#     temp_list = []
#     for line in text_file:
#         stripped_lines = line.strip()
#         print(stripped_lines)


filename = ("adventofcode22/input2-1.txt")
inputFile = open(filename, "r") # Åpner fil
steinSaksPapp = []# lager en liste 
for line in inputFile:
    strippedLines = line.rstrip()
    splittedLines = strippedLines.split()
    steinSaksPapp.append(splittedLines)

matchList = steinSaksPapp #[['A', 'Y'], ['B','X'], ['C','Z']]
points = 0

def winOrLose(opponent, contestant):
    if (opponent == 'A' and contestant == 'X') or (opponent == 'B' and contestant == 'Y') or (opponent == 'C' and contestant == 'Z'):
        return 3
    elif (opponent == 'A' and contestant == 'Y') or (opponent == 'B' and contestant == 'Z') or (opponent == 'C' and contestant == 'X'):
        return 6
    elif (opponent == 'A' and contestant == 'Z') or (opponent == 'B' and contestant == 'X') or (opponent == 'C' and contestant == 'Y'):
        return 0

def selectionPoint(chosenHand):
    if chosenHand == 'X':
        return 1
    elif chosenHand == 'Y':
        return 2
    elif chosenHand == 'Z':
        return 3

for i in range (len(matchList)):
    opponent = matchList[i][0]
    contestant = matchList[i][1]
    points += winOrLose(opponent, contestant)
    points += selectionPoint(contestant)

print(points)
