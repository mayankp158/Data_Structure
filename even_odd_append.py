class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """
    if head is None:
        return None
    even_start = None
    even_end = None
    odd_start = None
    odd_end = None
    current_node = head

    while current_node:
        next_node = current_node.next
        if current_node.data % 2 == 0:
            if even_start is None:
                even_start = current_node
                even_end = even_start
            else:
                even_end.next = current_node
                even_end = even_end.next
        else:

            if odd_start is None:
                odd_start = current_node
                odd_end = odd_start
            else:
                odd_end.next = current_node
                odd_end = odd_end.next

        current_node = next_node

    if odd_start is None:
        return even_start
    odd_end.next = even_start

    return odd_start


# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


def test_function(test_case):
    head = test_case[0]
    solution = test_case[1]

    node_tracker = dict({})
    node_tracker['nodes'] = list()
    temp = head
    while temp:
        node_tracker['nodes'].append(temp)
        temp = temp.next

    head = even_after_odd(head)
    temp = head
    index = 0
    try:
        while temp:
            if temp.data != solution[index] or temp not in node_tracker['nodes']:
                print("Fail")
                return
            temp = temp.next
            index += 1
        print("Pass")
    except Exception as e:
        print("Fail")

arr = [1, 2, 3, 4, 5, 6]
solution = [1, 3, 5, 2, 4, 6]

head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)


arr = [1, 3, 5, 7]
solution = [1, 3, 5, 7]

head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

arr = [2, 4, 6, 8]
solution = [2, 4, 6, 8]
head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)