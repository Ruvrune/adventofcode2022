class crates():
        def __init__(self, matrix=[]):
                self.__crateMatrix = matrix
                self.__listOfCrateColumns = self.createListFromColumn()

        def getMatrix(self):
                return self.__crateMatrix

        #Returnerer kolonnene i matrisen
        def getColumn(self, i):
                return [row[i] for row in self.__crateMatrix]

        def getListOfColumns(self):
                return self.__listOfCrateColumns

        #Putter kolonner fra matrisen inn i hver sin liste i en liste (Reversert, så siste kasse er sist i listen)
        def createListFromColumn(self):
                self.__listOfCrateColumns = []
                for i in range(len(self.__crateMatrix)+1):
                        columnToRow = self.getColumn(i)
                        tempRow = []
                        for j in reversed (range(len(columnToRow))):
                                if columnToRow[j]!='':
                                        tempRow.append(columnToRow[j])
                        self.__listOfCrateColumns.append(tempRow)                        
                return self.__listOfCrateColumns
                        
        #Henter ut kasse fra definert posisjon i matrisen (ikke relevant for programmet)
        def locateCrate(self, row, column):
                for i in range(len(self.__crateMatrix)):
                        for j in range(len(self.__crateMatrix)):
                                if i == row and j == column:
                                        print(self.__crateMatrix[i][j])
                                        
        def moveCrate(self, numberOfCrates, fromColumn, toColumn):  
                #Henter ut angitt antall kasser fra fra-kolonne (og fjerner fra liste) og appender de til til-kolonnen.
                if len(self.__listOfCrateColumns[fromColumn]) >= numberOfCrates:
                        movingList = self.__listOfCrateColumns[fromColumn][-numberOfCrates:]
                        self.__listOfCrateColumns[fromColumn] = self.__listOfCrateColumns[fromColumn][:-numberOfCrates]
                        for i in movingList:
                                self.__listOfCrateColumns[toColumn].append(i)

        def allLastCrates(self):
                lastList = []
                for i in range(len(self.__listOfCrateColumns)):
                     lastList.append(self.__listOfCrateColumns[i][-1])   
                return lastList
                                         
 
def main():
        filename = ("adventofcode22/input5-1.txt")
        inputFile = open(filename, "r") # Åpner fil     
        moveList = []
        for line in inputFile:
                #Stripper, splitter og henter ut tallene fra hver linje (et godt pythonisk eksempel)
                procedure  = [int(symbol) for symbol in line.rstrip().split() if symbol.isdigit()] 
                moveList.append(procedure)

        # matrix =[[ '',   '[D]', ''     ],   
        #          ['[N]', '[C]' ,   '' ],   
        #          ['[Z]', '[M]', '[P]']]

        
        matrix = [[ '' ,    '' ,   '' , '[C]',   '' ,   '',  '[N]', '[R]',   '' ],   
                  ['[J]', '[T]',   '' , '[H]',   '' ,   '',  '[P]', '[L]',   '' ],  
                  ['[F]', '[S]', '[T]', '[B]',   '' ,   '',  '[M]', '[D]',   '' ],   
                  ['[C]', '[L]', '[J]', '[Z]', '[S]',   '',  '[L]', '[B]',   '' ],  
                  ['[N]', '[Q]', '[G]', '[J]', '[J]',   '',  '[F]', '[F]', '[R]'],
                  ['[D]', '[V]', '[B]', '[L]', '[B]', '[Q]', '[D]', '[M]', '[T]'],
                  ['[B]', '[Z]', '[Z]', '[T]', '[V]', '[S]', '[V]', '[S]', '[D]'],
                  ['[W]', '[P]', '[P]', '[D]', '[G]', '[P]', '[B]', '[P]', '[V]']]         

        crateStack = crates(matrix)
        #Kjører flytteprosedyre fra liste
        for i in range(len(moveList)):
                crateStack.moveCrate(moveList[i][0],moveList[i][1]-1,moveList[i][2]-1)
        print(crateStack.allLastCrates())
      
       
if __name__ == '__main__':
      main()

