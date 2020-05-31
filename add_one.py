def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    borrow = 1
    for i in range(len(arr), 0, -1):

        digit = borrow + arr[i - 1]
        borrow = digit // 10
        if borrow == 0:
            arr[i - 1] = digit
            break
        elif borrow == 1:
            arr[i - 1] = digit % 10
    arr = [borrow] + arr

    pos = 0
    while arr[pos] == 0:
        pos = pos + 1
    return arr[pos:]


# A helper function for Test Cases
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")

# Test Case 1
arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)

# Test Case 2
arr = [1, 2, 3]
solution = [1, 2, 4]
test_case = [arr, solution]
test_function(test_case)

# Test Case 3
arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)