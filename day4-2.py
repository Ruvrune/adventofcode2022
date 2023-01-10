filename = ("adventofcode22/input4-1.txt")
inputFile = open(filename, "r") # Åpner fil
#pakkeListe = []# lager en liste 

def main():
        numberOfOverLaps = 0
        for line in inputFile:
                strippedLines = line.rstrip()
                firstElf, secondElf = strippedLines.split(",")
                listOneLength = elfRange(elfRangeValues(firstElf)[0],elfRangeValues(firstElf)[1])
                listTwoLength = elfRange(elfRangeValues(secondElf)[0],elfRangeValues(secondElf)[1])
                valueListOne = []
                valueListTwo = []
                for i in range(elfRangeValues(firstElf)[0],elfRangeValues(firstElf)[0]+listOneLength+1):
                          valueListOne.append(i)
                for i in range(elfRangeValues(secondElf)[0],elfRangeValues(secondElf)[0]+listTwoLength+1):
                          valueListTwo.append(i)
                numberOfOverLaps += overlap(valueListOne, valueListTwo)
        print (numberOfOverLaps)

def elfRangeValues(elf):
        elfFrom, elfTo = elf.split("-")
        return [int(elfFrom), int(elfTo)]

def elfRange(start, stop):
        return (stop-start)

def overlap(listOne, listTwo):
        overlapping = False
        numberOfMatches = 0
        #Sjekk om tallet befinner seg i begge liste, øk teller med 1 om det er minst ett tilfelle med treff
        for i in listOne:
                if i in listTwo:
                        overlapping = True
        if overlapping == True:
                numberOfMatches += 1
        return numberOfMatches
        
if __name__ == '__main__':
      main()