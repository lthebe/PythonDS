def selectionSort(theSeq):
    n = len(theSeq)
    for i in range(n-1):
        smallNdx = i
        for j in range(i+1, n):#check if any element aftrer i contains smaller value
            if theSeq[j] < theSeq[smallNdx]:
                smallNdx = j
        if smallNdx != i:
            tmp = theSeq[i]
            theSeq[i] = theSeq[smallNdx]
            theSeq[smallNdx] = tmp
