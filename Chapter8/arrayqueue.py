#circular array to implement Queue ADT - good for queue with fixed max size
#time complexities of all operation is O(1) unlike list based  implementation
#list based implementation has O(n) for enqueue and dequeue and O(1) for
#amortized complexity
import sys
sys.path.append("../")
from myarray import Array

class Queue:
    def __init__(self, maxSize):
        self._count = 0 #count the number of item
        self._front = 0 #front set to 0 in the beginning
        self._back = maxSize - 1 #back at the end in the beginning
        self._qArray = Array(maxSize) #array to hold item

    #returns if the queue is empty
    def isEmpty(self):
        return self._count == 0

    #returns true if the queue is full
    def isFull(self):
        return self._count == len(self._qArray)

    #returns the no of itmes in the queue
    def __len__(self):
        return self._count

    #adds the given item to the queue
    def enqueue(self, item):
        assert not self.isFull(), "Queue filled up"
        maxSize = len(self._qArray)
        self._back = (self._back + 1) % maxSize
        self._qArray[self._back] = item
        self._count += 1

    #removes and returns the first item
    def dequeue(self):
        assert not self.isEmpty(), "Queue is empty"
        item = self._qArray[self._front]
        maxSize = len(self._qArray)
        self._front = (self._front + 1) % maxSize
        self._count -= 1
        return item
