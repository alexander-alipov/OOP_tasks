from abc import ABC, abstractmethod

class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None
    
class StackInterface(ABC):
    
    @abstractmethod
    def push_back(self, obj):
        return -1  
            
    @abstractmethod  
    def pop_back(self):
        return -1 
    
class Stack(StackInterface):
    def __init__(self):
        self._top = None
        self._tail = None

    def push_back(self, obj):
        if self._top == None:
            self._top = self._tail = obj
        else:
            self._tail._next = obj
            self._tail = obj    

    def pop_back(self):
        node = self._top
        if self._top._next == None:
            self._top = self._tail = None
            return node
        while node._next._next != None:
            node = node._next
        last = node._next
        self._tail = node
        self._tail._next = None
        return last 
