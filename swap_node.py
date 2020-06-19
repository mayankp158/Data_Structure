class Node:
    """LinkedListNode class to be used for this problem"""
    def __init__(self, data):
        self.data = data
        self.next = None


"""
:param: head- head of input linked list
:param: `position_one` - indicates position (index) ONE
:param: `position_two` - indicates position (index) TWO
return: head of updated linked list with nodes swapped

TODO: complete this function and swap nodes present at position_one and position_two
Do not create a new linked list
"""


def swap_nodes(head, position_one, position_two):
    if position_one == position_two:
        return head

    current_one = None
    current_two = None
    previous_one = None
    previous_two = None
    current_index = 0
    current_node = head
    new_head = None

    while current_node:
        if current_index == position_one:
            current_one = current_node
        elif current_index == position_two:
            current_two = current_node
            break
        if current_one is None:
            previous_one = current_node
        previous_two = current_node
        current_node = current_node.next
        current_index = current_index + 1

    previous_two.next = current_one
    temp = current_one.next
    current_one.next = current_two.next
    current_two.next = temp

    if previous_one is None:
        new_head = current_two
    else:
        previous_one.next = current_two
        new_head = head
    return new_head


def test_function(test_case):
    head = test_case[0]
    left_index = test_case[1]
    right_index = test_case[2]

    left_node = None
    right_node = None

    temp = head
    index = 0
    try:
        while temp is not None:
            if index == left_index:
                left_node = temp
            if index == right_index:
                right_node = temp
                break
            index += 1
            temp = temp.next

        updated_head = swap_nodes(head, left_index, right_index)

        temp = updated_head
        index = 0
        pass_status = [False, False]

        while temp is not None:
            if index == left_index:
                pass_status[0] = temp is right_node
            if index == right_index:
                pass_status[1] = temp is left_node

            index += 1
            temp = temp.next

        if pass_status[0] and pass_status[1]:
            print("Pass")
        else:
            print("Fail")
        return updated_head
    except Exception as e:
        print("Fail")

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
        print(head.data, end=" ")
        head = head.next
    print()

arr = [3, 4, 5, 2, 6, 1, 9]
head = create_linked_list(arr)
left_index = 3
right_index = 4

test_case = [head, left_index, right_index]
updated_head = test_function(test_case)

arr = [3, 4, 5, 2, 6, 1, 9]
left_index = 2
right_index = 4
head = create_linked_list(arr)
test_case = [head, left_index, right_index]
updated_head = test_function(test_case)

arr = [3, 4, 5, 2, 6, 1, 9]
left_index = 0
right_index = 1
head = create_linked_list(arr)
test_case = [head, left_index, right_index]
updated_head = test_function(test_case)





















# def swap_nodes(head, left_index, right_index):
#     current = head
#     previous_1 = None
#     previous_2 = None
#     while current:
#         for _ in range(left_index):
#             current1 = current
#             temp = current_1.next
#             previous_1 = current[i - 1]
#
#             current = current.next
#         for _ in range(right_index):
#             current2 = current
#             previous_2 = current[i - 2]
#             current = current.next
#     current_1 = current2.next
#     previous_2 = current_1
#     previous_1 = current_2
#     current_2 = temp
#
#     return head