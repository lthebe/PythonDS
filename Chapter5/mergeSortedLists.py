def mergeSortedLists(listA, listB):
    newList = list()
    a = 0
    b = 0

    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            newList.append(listA[a])
            a += 1
        else:
            newList.append(listB[b])
            b += 1

    while a < len(listA):
        newList.append(listA[a])
        a += 1 #adds if list a has more items
    while b < len(listB):
        newList.append(listB[b])
        b += 1
    return newList
