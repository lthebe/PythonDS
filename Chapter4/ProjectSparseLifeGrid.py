class SparseLifeGrid():
    LIVE_CELL = 1
    DEAD_CELL = 0
    """Creates a new infinite-sized game grid. All cells in
    the grid are initially set to dead"""
    def __init__(self):
        self._elementList = list() #holds only the live cell

    """Returns a 2-tuple (minrow, mincol) that contains the mini-
    mum row index and the minimum column index that is currently occupied
    by a live cell."""
    def minRange(self):
        assert len(self._elementList) > 0, "Configure grid before using range!"
        minrow = self._elementList[0].row
        mincol = self._elementList[0].col
        for item in self._elementList:
            if minrow > item.row:
                minrow = item.row
            if mincol > item.col:
                mincol = item.col
        return minrow, mincol


    """Returns a 2-tuple (maxrow, maxcol) that contains the maxi-
    mum row index and the maximum column index that is currently occupied
    by a live cell."""
    def maxRange(self):
        assert len(self._elementList) > 0, "Configure grid before using range!"
        maxrow = self._elementList[0].row
        maxcol = self._elementList[0].col
        for item in self._elementList:
            if maxrow < item.row:
                maxrow = item.row
            if maxcol < item.col:
                maxcol = item.col
        return maxrow, maxcol

    """Configures the grid for evolving the first gen-
    eration. The coordList argument is a sequence of 2-tuples with each
    tuple representing the coordinates (r, c) of the cells to be set as alive. All
    remaining cells are cleared or set to dead."""
    def configure(self, coordList):
        self._elementList = list()
        for item in coordList:
            r, c = item #unpack the tuples
            element = _CellElement(r,c, self.LIVE_CELL)
            self._elementList.append(element)

    """Clears the individual cell (row, col) and sets it
    to dead. The cell indices must be within the valid range of the grid."""
    def clearCell(self, row, col):
        min_row, min_col = self.minRange()
        max_row, max_col = self.maxRange()
        assert (min_row <= row <= max_row) and (min_col <= col <= max_col), \
            "Cell within grid only can be cleared!"
        index = self._findPosition(row, col)
        if index is not None:
            self._elementList.pop(index)

    """Sets the indicated cell (row, col) to be alive. The
    cell indices must be within the valid range of the grid."""
    """The grid min and max range does not include the cell which is just
    outside the boundary and with three neighbors"""
    def setCell(self, row, col):
        min_row, min_col = self.minRange()
        max_row, max_col = self.maxRange()
        assert (min_row -1 <= row <= max_row + 1) and (min_col - 1 <= col <= max_col +1), \
            "Cell can be set only within grid! - and a step out of grid"
        element = _CellElement(row, col, self.LIVE_CELL)
        self._elementList.append(element)

    """Returns a boolean value indicating if the given
    cell (row, col) contains a live organism. The cell indices must be within
    the valid range of the grid."""
    def isLiveCell(self, row, col):
        #print row, col, "printed in isLiveCell"
        min_row, min_col = self.minRange()
        max_row, max_col = self.maxRange()
        #liveCell min_row, max_row, min_col, max_col changed by 1
        assert (min_row <= row <= max_row) and (min_col <= col <= max_col), \
            "Live cell can be checked within grid only"
        if self._findPosition(row, col) is not None:
            return True
        else:
            return False

    """Returns the number of live neighbors for
    the given cell (row, col). The neighbors of a cell include all of the cells
    immediately surrounding it in all directions. For the cells along the border
    of the grid, the neighbors that fall outside the grid are assumed to be dead.
    The cell indices must be within the valid range of the grid."""
    def numLiveNeighbors(self, row, col):
        count = 0#livecell counter
        min_row, min_col = self.minRange()
        max_row, max_col = self.maxRange()
        #LiveNeighbors is searched for the dead cell just outside of the grid
        assert (min_row -1 <= row <= max_row + 1) and (min_col - 1 <= col <= max_col +1), \
            "<minrow-1, mincol-1> to <maxrow+1, max_col+1>"
        for r in range(row - 1, row + 2):#as range includes only lower bound
            for c in range(col - 1, col + 2):
                if (r == row and c == col):
                    continue #neglect the same cell
                if (min_row <= r <= max_row) and (min_col <= c <= max_col):#all utside grid is dead cell
                    if self.isLiveCell(r,c):
                        count += 1
        return count


    def _findPosition(self, row, col):
        n = len(self._elementList)
        for i in range(n):
            if row == self._elementList[i].row and \
                    col == self._elementList[i].col:
                return i
        return None #None when nothing  found in that position


class _CellElement:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
