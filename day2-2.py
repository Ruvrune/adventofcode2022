
filename = ("adventofcode22/input2-1.txt")
inputFile = open(filename, "r") # Åpner fil
steinSaksPapp = []# lager en liste 
for line in inputFile:
    strippedLines = line.rstrip()
    splittedLines = strippedLines.split()
    steinSaksPapp.append(splittedLines)

matchList =  steinSaksPapp 
points = 0

def rockScissorPaper(opponent, utfall):
    if opponent == 'A':
        if utfall == 'X':
            return 'scissor'
        elif utfall == 'Y':
            return 'rock'
        elif utfall == 'Z':
            return 'paper'
    elif opponent == 'B':
        if utfall == 'X':
            return 'rock'
        elif utfall == 'Y':
            return 'paper'
        elif utfall == 'Z':
            return 'scissor'
    elif opponent == 'C':
        if utfall == 'X':
            return 'paper'
        elif utfall == 'Y':
            return 'scissor'
        elif utfall == 'Z':
            return 'rock'

def winOrLose(opponent, contestant):
    if (opponent == 'A' and contestant == 'rock') or (opponent == 'B' and contestant == 'paper') or (opponent == 'C' and contestant == 'scissor'):
        return 3
    elif (opponent == 'A' and contestant == 'paper') or (opponent == 'B' and contestant == 'scissor') or (opponent == 'C' and contestant == 'rock'):
        return 6
    elif (opponent == 'A' and contestant == 'scissor') or (opponent == 'B' and contestant == 'rock') or (opponent == 'C' and contestant == 'paper'):
        return 0

def selectionPoint(chosenHand):
    if chosenHand == 'rock':
        return 1
    elif chosenHand == 'paper':
        return 2
    elif chosenHand == 'scissor':
        return 3

for i in range (len(matchList)):
    opponent = matchList[i][0]
    utfall = matchList[i][1]

    points += winOrLose(opponent, rockScissorPaper(opponent, utfall))
    points += selectionPoint(rockScissorPaper(opponent, utfall) )

print(points)
