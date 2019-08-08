#The file containing the sudoku class and any way of getting in sudokus.
import rsolve
class Sudoku(object):
    
    def __init__(self):
        self.sudokuGrid = {}
        self.rows = ["A","B","C","D","E","F","G","H","I"]
        self.columns = ["1","2","3","4","5","6","7","8","9"]

    def inputFromFile(self,input):
        row = 0
        column = 0
        for each in list(input):
            if column == 9:
                column = 0
                row += 1
            if each != ".":
                self.sudokuGrid["{0}{1}".format(self.rows[row],self.columns[column])] = int(each)
            else:
                self.sudokuGrid["{0}{1}".format(self.rows[row],self.columns[column])] = " "
            column += 1

    def solveByRecursion(self):
        self.inputFromList(rsolve.solve(self.getBoard()))
        self.show()

    def solveByRRecursion(self):
        self.inputFromList(rsolve.rsolve(self.getBoard()))
        self.show()

    def inputFromList(self,input):
        #collapse 2d
        new = []
        for row in input:
            for i in row:
                new.append(i)
        #add to dictionary
        row = 0
        column = 0
        for i in new:
            if column == 9:
                column = 0
                row += 1
            self.sudokuGrid["{0}{1}".format(self.rows[row],self.columns[column])] = int(i)
            column += 1

    def getRow(self,rowNumber):
        rowletter = self.rows[rowNumber-1]
        row = []
        for k,v in self.sudokuGrid.items():
            if rowletter in k:
                row.append(v)
        return row

    def getColumn(self,columnNumber):
        column = []
        for k,v in self.sudokuGrid.items():
            if columnNumber in k:
                column.append(v)
        return column

    def getBox(self,boxNumber):
        box = []
        if boxNumber % 3 == 1:
            a = 0
        if boxNumber % 3 == 2:
            a = 3
        if boxNumber % 3 == 0:
            a = 6
        if boxNumber / 3 <= 1:
            b = 1
        elif boxNumber / 3 <= 2:
            b = 4
        elif boxNumber / 3 <= 3:
            b = 7
        for i in range(a,a+4):
            for j in range(b,b+4):
                box.append(self.sudokuGrid["{0}{1}".format(self.rows[a],str(b))])
        return box

    def getBoard(self):
        board = []
        for each in range(1,10):
            board.append(self.getRow(each))
        return board

    def showRow(self,rowNumber):
        row = self.getRow(rowNumber)
        print(row)
    
    def showColumn(self,columnNumber):
        column = self.getColumn(columnNumber)
        print(column)

    def showBox(self,boxNumber):
        box = self.getBox(boxNumber)
        print(box)

    def show(self):
        a = 1
        s = ["\n"]
        for k,v in self.sudokuGrid.items():
            s.append(str(v))
            s.append(" ")
            if a % 3 == 0 and a % 9 != 0:
                s.append("|")
            if a % 9 == 0:
                s.append("\n")
            if a % 27 == 0 and a % 81 != 0:
                s.append("------+------+------\n")
            a += 1
        print("".join(s))