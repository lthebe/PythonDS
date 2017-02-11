#implementation of multiarray ADT using 1-D array
import sys
sys.path.append('../')
from myarray import Array
class MultiArray:
    def __init__(self, *dimensions):
        assert len(dimensions) > 1, "Dimensions can not be less than 1"
        self._dims = dimensions
        size = 1
        for d in dimensions:
            assert d > 0, "Dimensions should be greater than 0"
            size *= d
        #create a 1-D array to store all elements
        self._elements = Array(size)
        #create 1-D array to store the equation factors
        self._factors = Array(len(dimensions))
        self._computeFactors()
    #no of dimensions in the array
    def numDims(self):
        return len(self._dims)

    #returns the lenth of the given dimension
    def length(self, dim):
        assert dim >= 1 and dim <= len(self._dims),\
               "Dimension component out of range"
        return self._dims[dim-1]

    #def clears the array by setting all elements to value
    def clear(self, value):
        self._elements.clear(value)

    #returns the cotnest of element(i_1, i_2,..., i_n)
    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == self.numDims(), "Invalid array subscripts!"
        index = self._computeIndex(ndxTuple)
        assert index is not None, "Array subscript out of range"
        return self._elements[index]

    #sets the contents of element(i_1, i_2, i_3,...i_n)
    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == self.numDims(), "Invalid # of array subscripts"
        index = self._computeIndex(ndxTuple)
        assert index is not None, "Array subscript out of range"
        self._elements[index] = value

    #computes a 1-D array offset for element (i_1, i_2, ...i_n)
    #using the equation i_1 * f_1 + i_2 * f_2 +.... + i_n * f_n
    def _computeIndex(self, idx):
        offset = 0
        for j in range(len(idx)):
            #make sure the index componens within the legal range
            if idx[j] < 0 or idx[j] >= self._dims[j]:
                return None
            else:
                offset += idx[j] * self._factors[j]
        return offset

    #computes the factor values used in the index equation
    #done as part of exercise
    def _computeFactors(self):
        self._factors[len(self._factors)-1] = 1
        for j in reversed(range(len(self._factors) - 1)):
            self._factors[j] = self._factors[j+1] * self._dims[j+1]
