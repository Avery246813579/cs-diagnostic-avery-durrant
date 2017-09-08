class List:
    start = None

    def add(self, element):
        if self.start is None:
            self.start = Node(element)
            return

class Node:
    target = None

    def __init__(self, value):
        self.value = value

    def next(self):
        return self.target