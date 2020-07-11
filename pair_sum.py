def pair_sum(arr, target):
    """
    :param: arr - input array
    :param: target - target value
    TODO: complete this method to find two numbers such that their sum is equal to the target
    Return the two numbers in the form of a sorted list
    """
    # ans = []
    # sum = 0
    # for a in range(len(arr)):
    #     temp = arr[a]
    #     for b in range(len(arr)):
    #         sum = temp + arr[b]
    #         if sum == target and a != b:
    #             ans.append(arr[b])
    #             ans.append(arr[a])
    #             return ans
    #         break
    #
    #         pair_sum(arr, target)

    arr.sort()
    front_index = 0
    last_index = (len(arr)-1)

    while front_index<last_index:
        if arr[front_index] + arr[last_index] == target:
            return [arr[front_index],arr[last_index]]
        if arr[front_index] + arr[last_index] < target:
            front_index+=1
        else:
            last_index-=1

    return [None,None]

def test_function(test_case):
    input_list = test_case[0]
    target =test_case[1]
    solution = test_case[2]
    output = pair_sum(input_list, target)
    if output == solution:
        print("Pass")
    else:
        print("False")

input_list = [2, 7, 11, 15]
target = 9
solution = [2, 7]
test_case = [input_list, target, solution]
test_function(test_case)

input_list = [0, 8, 5, 7, 9]
target = 9
solution = [0, 9]
test_case = [input_list, target, solution]
test_function(test_case)

input_list = [110, 9, 89]
target = 9
solution = [None, None]
test_case = [input_list, target, solution]
test_function(test_case)