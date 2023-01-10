import string

def main():

    filename = ("adventofcode22/input3-1.txt")
    inputFile = open(filename, "r") # Åpner fil
    pakkeListe = []# lager en liste 
    priorityList = list(string.ascii_letters) #Lager liste med alfabet, først små, så store bokstaver
    ruckSackSum = 0

    for line in inputFile:
        strippedLines = line.rstrip()
        pakkeListe.append(strippedLines)

    for rucksack in pakkeListe:
        compartmentSize = int(len(rucksack)/2)
        firstCompartment = set(rucksack[0:compartmentSize])
        secondCompartment = set(rucksack[compartmentSize:len(rucksack)])
        #Legger til prioritetsnummer til sum
        ruckSackSum += (priorityList.index(setResult((firstCompartment.intersection(secondCompartment))))+1)

    print (ruckSackSum)

def setResult(setComparison):
    #Returner bokstaven fra sett-sammenligning (uten {}-klammer), hvis det er en match i settet. Ellers returner blankt
    if len(setComparison)==1:
        for match in setComparison:
            return(match)         
    else:
        return

if __name__ == '__main__':
      main()
