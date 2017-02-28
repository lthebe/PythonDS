#Implementation of the Queue ADT using a linked list

class Queue:
    def __init__(self):
        self._qhead = None
        self._qtail = None
        self._count = 0

    #Returns true if the queue is empty
    def isEmpty(self):
        return self._qhead is None

    #Returns the number of items
    def __len__(self):
        return self._count

    #adds the given item to the queue
    def enqueue(self, item):
        node = _QueueNode(item)
        if self.isEmpty():
            self._qhead = node
        else:
            self._qtail.next = node

        self._qtail = node
        self._count += 1

    #Removes and returns the first item
    def dequeue(self):
        assert not self.isEmpty(), "Can not be empty"
        node = self._qhead
        if self._qhead is self._qtail:
            self._qtail = None
        self._qhead = self._qhead.next
        self._count -= 1
        return node.item

class _QueueNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None
