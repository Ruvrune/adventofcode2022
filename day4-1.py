filename = ("adventofcode22/input4-1.txt")
inputFile = open(filename, "r") # Åpner fil
#pakkeListe = []# lager en liste 

def main():
        numberOfMatches = 0
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
                check = all(item in valueListOne for item in valueListTwo) or all(item in valueListTwo for item in valueListOne)
                if check is True:
                        numberOfMatches += 1
        print(numberOfMatches)

def elfRangeValues(elf):
        elfFrom, elfTo = elf.split("-")
        return [int(elfFrom), int(elfTo)]

def elfRange(start, stop):
        return (stop-start)

if __name__ == '__main__':
      main()