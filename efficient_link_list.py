class Node:
    def __init__(self,value):
        self.value= value
        self.next = None

def efficient(link_list):
    head=None
    tail=None
    for value in link_list:
        if head is None:
            head=Node(value)
            tail=head
        else:

            tail.next=Node(value)
            tail=tail.next
    return head
link_list = [1, 2, 3, 4, 5, 6]
head = efficient(link_list)
print(head.next.value)