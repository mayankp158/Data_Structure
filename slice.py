# a = ("a", "b", "c", "d", "e", "f", "g", "h")
# x = slice(3,None)
# print(a[x])
#
# a = ['c']
# c = 'b'
# b = [a[0] + c]
# d = [c + a[0]]
# print(b + d)

# small_output = ['c']
# subString = 'c'
# current_char = 'b'
# for index in range(len(small_output[0]) + 1):
#     new_subString = subString[: index] + current_char + subString[index:]
#     print(new_subString)
#     print(index)


# a = ['']
# b = 'c'
# for i in range(len(a) + 1):
#     d = a[i] + b
# print(d)
def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""
def keypad(num):
    # Base case
    if num <= 1:

        return [""]

    # If `num` is single digit, get the LIST having one element - the associated string
    elif 1 < num <= 9:

        return list(get_characters(num))


    # Otherwise `num` >= 10. Find the unit's (last) digits of `num`
    last_digit = num % 10
    print(last_digit)

    '''Step 1'''
    # Recursive call to the same function with “floor” of the `num//10`

    small_output = keypad(num // 10)  # returns a LIST of strings
    print(small_output)


    '''Step 2'''
    # Get the associated string for the `last_digit`
    keypad_string = get_characters(last_digit)  # returns a string
    print(keypad_string)
    '''Permute the characters of result obtained from Step 1 and Step 2'''
    output = list()

    '''
    The Idea:
    Each character of keypad_string must be appended to the 
    end of each string available in the small_output
    '''
    for character in keypad_string:
        for item in small_output:
            new_item = item + character
            print(new_item)
            output.append(new_item)

    return output  # returns a LIST of strings


def test_keypad(input, expected_output):
    if sorted(keypad(input)) == expected_output:
        print("Yay. We got it right.")
    else:
        print("Oops! That was incorrect.")


# Example case
input = 354
expected_output = sorted(["djg", "ejg", "fjg", "dkg", "ekg", "fkg", "dlg", "elg", "flg", "djh", "ejh", "fjh", "dkh", "ekh", "fkh", "dlh", "elh", "flh", "dji", "eji", "fji", "dki", "eki", "fki", "dli", "eli", "fli"])
test_keypad(input, expected_output)
# def permutations(string):
#     """
#     :param: input string
#     Return - list of all permutations of the input string
#     TODO: complete this function to return a list of all permutations of the string
#     """
#     final = []
#     d = []
#
#
#     if len(string) == 0:
#         final.append('')
#     else:
#         first = string[0]
#         after = string[1:]
#         sub_compound = permutations(after)
#         b = [sub_compound[0] + first]
#         c = [first + sub_compound[0]]
#
#         d = b + c
#
#     return d
#
#
# def test_function(test_case):
#     string = test_case[0]
#     solution = test_case[1]
#     output = permutations(string)
#
#     output.sort()
#     solution.sort()
#
#     if output == solution:
#         print("Pass")
#     else:
#         print("Fail")
#
# string = 'ab'
# solution = ['ab', 'ba']
# test_case = [string, solution]
# test_function(test_case)
