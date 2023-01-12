class programExecution():
        def __init__(self):
                self.__value = 1
                self.__cycle = 0
                self.__signalStrength = []

        def getCycles(self):
                return self.__cycle
        
        def getValue(self):
                return self.__value

        def getSignalStrength(self):
                return self.__signalStrength
        
        def runInstrunction(self, instruction, value, checkpointList):
                cycles = 0
                if instruction == 'noop':
                        while cycles < 1:
                                self.__cycle += 1
                                cycles += 1
                                self.checkpoints(checkpointList)
                                
                elif instruction == 'addx':
                        while cycles < 2:
                                self.__cycle += 1
                                cycles += 1
                                self.checkpoints(checkpointList)
                        self.__value += value
                        
        #Legger til verdiene for de angitte checkpointene i lista over signalstyrke:
        def checkpoints(self, checkpoints):
                for i in range(len(checkpoints)):
                        if self.__cycle == checkpoints[i]:
                                self.__signalStrength.append(self.__value * self.__cycle)

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
        checkpointList = [20, 60, 100, 140, 180, 220]
        for i in range(len(instructionList)):
                if noopOrAddx(instructionList[i][0]):
                        runProgram.runInstrunction('noop',0, checkpointList)
                else:
                        value = int(instructionList[i][1])
                        runProgram.runInstrunction('addx',value, checkpointList)

        print(sum(runProgram.getSignalStrength()))

if __name__ == '__main__':
      main()

