from my2darray import Array2D #lifegrid adt uses two dimensional array

class LifeGrid:
    #defines constants to represt the cell states
    DEAD_CELL = 0
    LIVE_CELL = 1

    def __init__(self, numRows, numCols):
        self._grid = Array2D(numRows, numCols)
        #clear the grid and set all cells to dead
        self.configure(list())

    def numRows(self):
        return self._grid.numRows()

    def numCols(self):
        return self._grid.numCols()

    def configure(self, coordList):
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self.clearCell(i,j)
        #after setting all cell dead, set from coordlist alive
        for coord in coordList:
            self.setCell(coord[0], coord[1])
    #check if cell is alive
    def isLiveCell(self, row, col):
        return self._grid[row, col] == self.LIVE_CELL

    #clears the indicated cell by setting it to dead
    def clearCell(self, row, col):
        self._grid[row, col] = self.DEAD_CELL
    #sets the indicated cell to be alive
    def setCell(self, row, col):
        self._grid[row, col] = self.LIVE_CELL

    def numLiveNeighbors(self, row, col):
        count = 0#livecell counter
        upper_bound = row - 1 if row > 0 else row
        left_bound = col - 1 if col > 0 else col
        right_bound = col + 1 if col < (self.numCols() - 1) else self.numCols()-1
        lower_bound =  row + 1 if row < (self.numRows() - 1) else self.numRows() - 1

        for i in  range(upper_bound, lower_bound +1):
            for j in range(left_bound, right_bound + 1):
                if (i == row and j == col):
                    continue
                if self.isLiveCell(i, j):
                    count += 1
        return count
