def insertionSort(theSeq):
    n = len(theSeq)
    #starts with the first item as the only sorted entry
    for i in range(1,n):#first item is sorted
        value = theSeq[i]#save the value to be positioned
        #find the position where value fits in the ordered part of the list
        pos = i
        while pos > 0 and value < theSeq[pos-1]:
            theSeq[pos] = theSeq[pos-1]
            pos -= 1
        theSeq[pos] = value
