import sys
sys.path.append('../')
from myarray import Array
from multidimensionalarray import MultiArray
class ReportGenerator:
    def __init__(self, fileName):
        self._fileName = fileName
        self._inputFO = None #file object
        self._multiarray = MultiArray(5,20,12)

    def open(self):
        self._inputFO = open(self._fileName, "r")

    def close(self):
        self._inputFO.close()
        self._inputFO = None

    def load_data(self):
        self.open()
        for line in self._inputFO:
            words = line.split()
            if len(words) == 2:
                item_counter = 0
                f_index = int(words[1][1]) - 1#store index
            if len(words) == 13:
                if words[0] == "Item#":
                    pass
                else:
                    for i in range(12):
                        self._multiarray[f_index, item_counter, i] = float(words[i+1])
                    item_counter += 1
        self.close()
        return self._multiarray


rg = ReportGenerator('SalesData') #creates the report generator object to read SalesData
salesData = rg.load_data() #returns the filled in multi array as SalesData
# Compute the total sales of all items for all months in a given store.
def totalSalesByStore( salesData, store ):
# Subtract 1 from the store # since the array indices are 1 less
# than the given store #.
    s = store-1
    # Accumulate the total sales for the given store.
    total = 0.0
    # Iterate over item.
    for i in range( salesData.length(2) ):
        # Iterate over each month of the i item.
        for m in range( salesData.length(3) ):
            total += salesData[s, i, m]
    return total

# Compute the total sales of all items in all stores for a given month.
def totalSalesByMonth( salesData, month ):
# The month number must be offset by 1.
    m = month - 1
    # Accumulate the total sales for the given month.
    total = 0.0
    # Iterate over each store.
    for s in range( salesData.length(1) ):
    # Iterate over each item of the s store.
        for i in range( salesData.length(2) ):
            total += salesData[s, i, m]
    return total

# Compute the total sales of a single item in all stores over all months.
def totalSalesByItem( salesData, item ):
# The item number must be offset by 1.
    i = item - 1
    # Accumulate the total sales for the given month.
    total = 0.0
    # Iterate over each store.
    for s in range( salesData.length(1) ):
    # Iterate over each month of the s store.
        for m in range( salesData.length(3) ):
            total += salesData[s, i, m]
    return total

# Compute the total sales per month for a given store. A 1-D array is
# returned that contains the totals for each month.
def totalSalesPerMonth( salesData, store ):
# The store number must be offset by 1.
    s = store - 1
    # The totals will be returned in a 1-D array.
    totals = Array( 12 )
    # Iterate over the sales of each month.
    for m in range( salesData.length(3) ):
        sum = 0.0
        # Iterate over the sales of each item sold during the m month.
        for i in range( salesData.length(2) ):
            sum += salesData[s, i, m]
        # Store the result in the corresponding month of the totals array.
        totals[m] = sum
    # Return the 1-D array.
    return totals
print totalSalesByStore(salesData,1) #print stores 1 total sell
print totalSalesByItem(salesData, 2)#print items 2 total sell
print totalSalesByMonth(salesData, 4) #print months April total sell
salespermonth = totalSalesPerMonth(salesData, 1)#store1 total sell in each month
for a in range(len(salespermonth)):
    print salespermonth[a]
