class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
class Linked_list:
    def __init__(self):
        self.head = None
    def append(self,value):
        if self.head is None:
            self.head = Node(value)
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(value)
        return
# linked_list = Linked_list()
# linked_list.append(1)
# linked_list.append(2)
# linked_list.append(4)
    def to_list(self):
        list = []
        current_node = self.head
        while current_node:
            list.append(current_node.value)
            current_node = current_node.next
        return list
linked_list = Linked_list()
linked_list.append(1)
linked_list.append(2)
linked_list.append(4)
print(linked_list.to_list())