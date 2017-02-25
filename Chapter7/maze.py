#implement the MazeADT using a 2-D array
from __future__ import print_function
import sys
sys.path.append('../')
from my2darray import Array2D
from lliststack import Stack

class Maze:
    #Define constants to represent cell content
    MAZE_WALL = '*'
    PATH_TOKEN = 'X'
    TRIED_TOKEN = 'o'

    #Creates a maze object
    def __init__(self, numRows, numCols):
        self._mazeCells = Array2D(numRows, numCols)
        self._startCell = None
        self._exitCell = None

    #Returns the number of rows
    def numRows(self):
        return self._mazeCells.numRows()

    #Returns the number of columns
    def numCols(self):
        return self._mazeCells.numCols()

    #Fills the indicated cell with a wall marker
    def setWall(self, row, col):
        assert row >= 0 and row < self.numRows() and \
            col >= 0 and col < self.numCols(), "Cell index out of range"
        self._mazeCells[row, col] = self.MAZE_WALL


    #sets the starting cell position
    def setStart(self, row, col):
        assert row >= 0 and row < self.numRows() and \
            col >= 0 and col < self.numCols(), "Cell index out of range"
        self._startCell = _CellPosition(row, col)

    #sets the exit cell position
    def setExit(self, row, col):
        assert row >= 0 and row < self.numRows() and \
            col >= 0 and col < self.numCols(), "Cell index out of range"
        self._exitCell = _CellPosition(row, col)

    #attempts to solve the maze by finding path from start to exit
    #returns True if found, otherwise False
    #stack contains the _CellPosition items,
    def findPath(self):
        s = Stack()#stack to save the path
        s.push(self._startCell)
        self._markPath(self._startCell.row, self._startCell.col)
        while True:
            #inside the loop where neighbor cell is checked for valid move
            #same time, checked if we get the exit
            if s.isEmpty():
                return False
            current_cell = s.peek()
            row = current_cell.row
            col = current_cell.col
            if not self._exitFound(row, col):
                for r in [row-1, row, row+1]:
                    if not (current_cell.row == s.peek().row and \
                            current_cell.col == s.peek().col):
                        break
                    for c in [col-1, col, col+1]:
                        if ((r == row) ^ (c == col)):
                            if self._validMove(r,c):
                                self._markPath(r,c)
                                s.push(_CellPosition(r,c))
                                break
                if current_cell.row == s.peek().row and\
                        current_cell.col == s.peek().col:
                    not_in_path = s.pop()
                    self._markTried(not_in_path.row, not_in_path.col)

            else:
                return True

    #Resets the maze by removing all "path" and "tried" tokens
    def reset(self):
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                if self._mazeCells[r,c] == self.PATH_TOKEN or \
                        self._mazeCells[r,c] == self.TRIED_TOKEN:
                    self._mazeCells.clear()

    #prints a text represenation of the maze
    def draw(self):
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                if self._mazeCells[r,c] is not None:
                    print(self._mazeCells[r,c], sep = ' ', end= ' ')
                else:
                    if self._startCell.row == r and self._startCell.col == c:
                        print('s', sep = ' ', end = ' ')
                    elif self._exitCell.row == r and self._exitCell.col == c:
                         print('e', sep = ' ', end = ' ')
                    else:
                        print('.', sep = ' ', end = ' ')
            print ('\n')
        print ("--------------------------")

    #Returns True if the given cell position is a valid move
    def _validMove(self, row, col):
        return row >= 0 and row < self.numRows()\
            and col >= 0 and col < self.numCols()\
            and self._mazeCells[row, col] is None

    #Helper method to find if exit was found
    def _exitFound(self, row, col):
        return row == self._exitCell.row and \
            col == self._exitCell.col

    #Drops a "tried" token at the given cell
    def _markTried(self, row, col):
        self._mazeCells[row, col] = self.TRIED_TOKEN

    #Drops a "path" token at the given cell
    def _markPath(self, row, col):
        self._mazeCells[row, col] =self.PATH_TOKEN

#Private storage class for holding a cell position
class _CellPosition(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col
