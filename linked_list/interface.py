from node import Node

class AbstractLinkedList(object):
    """
    Abstract class representing the LinkedList inteface you must respect.

    You must not implement any of the method in this class, and this class
    must never be instantiated. It's just a "guide" of which methods
    the LinkedList class should respect.
    """
    
    def __init__(self, elements=None):
        self.elements = elements
        self.start = None
        self.end = None
        
        if self.elements:
            for element in self.elements:
                self.append(element)
        

    def __str__(self):
        return "[{}]".format(", ".join(strp(x) for x in self.elements)) if self.elements == None else "[]"
                

    def __len__(self):
        return self.count()

    def __iter__(self):
        raise NotImplementedError()

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError
            
        wantnode = self.start
        for i in range(index):
            wantnode.next
        return wantnode.elem

    def __add__(self, other):
        raise NotImplementedError()

    def __iadd__(self, other):
        raise NotImplementedError()

    def __eq__(self, other):
        raise NotImplementedError()

    def __ne__(self, other):
        raise NotImplementedError()

    def append(self, element):
        new_node = Node(element)
        #new_node.set_start = self.start
        #new_node.set_next = self.end
        #self.start = new_node
        #self.end=new_node.next
        if self.start is None:
            self.start = new_node
            self.end = new_node
        else:
            self.end.next = new_node
            self.end = new_node

    def count(self):
        if self.start:
            counter = 1
            tempNode = self.start
            while tempNode.next:
                counter += 1
                tempNode = tempNode.next
            return counter
        else:
            return 0

    def pop(self, index=None):
        raise NotImplementedError()
