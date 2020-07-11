def sort_012(input_list):
    zero = 0
    two = (len(input_list) - 1)

    front_index = 0

    while (front_index <= two):

        if input_list[front_index] == 0:
            input_list[front_index] = input_list[zero]
            input_list[zero] = 0
            zero+=1
            front_index+=1

        if input_list[front_index] == 2:
            input_list[front_index] = input_list[two]
            input_list[two] = 2
            two -= 1
        else:
            front_index+=1

def test_function(test_case):
    sort_012(test_case)
    print(test_case)
    if test_case == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_case = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
test_function(test_case)

test_case = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
test_function(test_case)

test_case = [2, 2, 0, 0, 2, 1, 0, 2, 2, 1, 1, 1, 0, 1, 2, 0, 2, 0, 1]
test_function(test_case)
