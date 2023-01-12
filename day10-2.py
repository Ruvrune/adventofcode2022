class programExecution():
        def __init__(self):
                self.__value = 1      #Sprite-variabel, generert fra angitt kommando per cycle
                self.__cycle = 0 
                self.__pixelCount = 0 #Generator-teller. Teller fra 0 til 39 per linje.
                self.g = self.CRTgenerator()

        def getCycles(self):
                return self.__cycle
        
        def getValue(self):
                return self.__value

        def runInstrunction(self, instruction, value):
                cycles = 0
                if instruction == 'noop':
                        while cycles < 1:
                                self.__cycle += 1
                                cycles += 1
                                next(self.g)                                            
                elif instruction == 'addx':
                        while cycles < 2:
                                self.__cycle += 1
                                cycles += 1
                                next(self.g)
                        self.__value += value
                                        
#Skriver ut en pixel per cycle. Siden bredden på sprite fra instruksjonene er 3, sammenlignes pixeltelleren med den angitte variabelen +-1.
#Ny linje ved hvert 40. tegn
        def CRTgenerator(self):       
                while True:
                        try:
                                while self.__pixelCount < 40:
                                        #Hvis treff mellom pixel-telleren og sprite med bredde på 3.
                                        if self.__pixelCount == self.__value  or self.__pixelCount == self.__value + 1 or self.__pixelCount == self.__value - 1:
                                                yield print('#', end='')
                                        else:
                                                #Blank skjerm
                                                yield print('.',end='')
                                        self.__pixelCount += 1
                        except StopIteration:
                                self.__pixelCount = 0
                                break
                        #Print linjeskift og nullstill generator for neste linje
                        print('')
                        self.__pixelCount = 0
                                                        
def noopOrAddx (instruction):
        if instruction == 'noop':
                return True
        elif instruction == 'addx':
                return False
       
def main():
        filename = ("adventofcode22/input10-1.txt")
        inputFile = open(filename, "r") # Åpner fil     
        instructionList = []
        for line in inputFile:
                #Stripper, splitter og henter ut kommandoer og tall fra hver linje i tekst-fil
                instructionList.append([(command) for command in line.rstrip().split()])
        
        runProgram = programExecution()

        for i in range(len(instructionList)):
                if noopOrAddx(instructionList[i][0]):
                        runProgram.runInstrunction('noop',0)
                else:
                        value = int(instructionList[i][1])
                        runProgram.runInstrunction('addx',value)
        
        
if __name__ == '__main__':
      main()

