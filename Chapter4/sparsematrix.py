#Implementation of Sparse matrix adt based on list
class SparseMatrix:
    def __init__(self, numRows, numCols):
        self._numRows = numRows
        self._numCols = numCols
        self._elementList = list()

    #return the no of rows in matrix
    def numRows(self):
        return self._numRows

    #return the number of columns in the matrix
    def numCols(self):
        return self._numCols

    #return the value of element (i,j):x[i,j] #implemented by me
    def __getitem__(self, ndxTuple):
        ndx = self._findPosition(ndxTuple[0], ndxTuple[1])
        if ndx:
            return self._elements[ndx].value
        else:
            return ndx #returns None

    #set the value of element i,j to the value s: x[i,j] = s
    def __setitem__(self, ndxTuple, scalar):
        ndx = self._findPosition(ndxTuple[0], ndxTuple[1])
        if ndx is not None: #element is found in the list
            if scalar != 0.0:
                self._elementList[ndx].value = scalar
            else:
                self._elementList.pop(ndx)
        else:#if the element is zero and not in the list
            if scalar != 0.0:
                element = _MatrixElement(ndxTuple[0], ndxTuple[1], scalar)
                self._elementList.append(element)

    #scale by the given scalar
    def scaleBy(self, scalar):
        for item in self._elementList:
            item.value *= scalar

    def __add__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and \
            rhsMatrix.numCols() == self.numCols(), "Matrix should be same size\
            for add operation!"
        nexMatrix = SparseMatrix(self.numRows(), self.numCols()) #newmatrix of same size
        #elements are  mutable, so the values are used to create new element and
        #copied to the new matrix
        for element in self._elementList:
            dupElement = _MatrixElement(element.row, element.col, element.value)
            newMatrix._elementList.append(dupElement)
        #now iteratne rhsMatrix for non zero value
        for element in rhsMatrix._elementList:
            value = newMatrix[element.row, element.col]
            value += element.value
            newMatrix[element.row, element.col] = value
        return newMatrix
    """The above implemention is O(k^2) in worst  case where k is the numuber
    of non zero elements in sparse matrix.  And way better than O(n^2) for
    k << mxn - if k is nearly equal to mxn, it would be m2n2 (way worst than n2)
    """

    def __sub__(self, rhsMatrix):
        pass

    def __mul__(self, rhsMatrix):
        pass

    def _findPosition(self, row, col):
        n = len(self._elementList)
        for i in range(n):
            if row == self._elementList[i].row and \
                    col == self._elementList[i].col:
                return i #return the index of the element if found
        return None #return None when the element is zero

    #storage class for holding non-zero matrix elements
class _MatrixElement:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
