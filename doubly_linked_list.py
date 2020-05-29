class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.previous = None
class Doubly:
    def __init__(self):
        self.head =None
        self.tail=None
    def append(self,value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        self.tail.next = Node(value)
        self.tail.previous = self.tail
        self.tail = self.tail.next
        return
    def unpack(self):
        list = []
        current_node = self.head
        while current_node:
            list.append(current_node.value)
            current_node = current_node.next
        return list
link_list = Doubly()
link_list.append(1)
link_list.append(2)
link_list.append(3)

print(link_list.unpack())