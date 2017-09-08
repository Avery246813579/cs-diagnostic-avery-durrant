class LinkedList:
    head = None

    def add(self, element):
        if self.head is None:
            self.head = Node(element)
            return
        
        new_start = Node(element)
        new_start.pointer = self.head
        self.head = new_start
        
    def pop(self):
        if self.head is None:
            return
        
        self.head = self.head.next()

    def reverse(self):
        if self.head is None:
            return

        next = self.head.next()
        self.head.pointer = None

        while True:
            if next is None:
                break

            current = next
            next = current.next()

            current.pointer = self.head
            self.head = current

    def __str__(self):
        if self.head is None:
            return "Empty"
        
        to_return = ""
        current = self.head
        while True:
            to_return += str(current.value) + " "
            
            next_node = current.next()
            if next_node is None:
                break
            
            current = next_node

        return to_return


class Node:
    pointer = None

    def __init__(self, value):
        self.value = value

    def next(self):
        return self.pointer

list = LinkedList()
list.add(1)
list.add(2)
list.add(3)
list.add(4)

print(list)

list.reverse()

print(list)