#implementation of the Stack ADT using list
class Stack:
    #creates empty stack
    def __init__(self):
        self._theItems = list()

    #Returns true if the stack is empty
    def isEmpty(self):
        return len(self) == 0

    #returns the no of items in the stack
    def __len__(self):
        return len(self._theItems)

    #returns the top item of the stack without removing it
    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self._theItems[-1]

    #removes and returns the top item on the stack
    def pop(self):
        assert not self.isEmpty(), "Cannot pop from  empty stack"
        return self._theItems.pop()
    #push an item onto the top of the stack
    def push(self, item):
        self._theItems.append(item)
