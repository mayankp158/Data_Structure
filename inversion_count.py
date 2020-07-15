def count(arr):
    n = len(arr)
    temp = [0] * n
    return mergesort(arr, temp, 0, n - 1)


def mergesort(arr, temp, left, right):
    invc = 0
    if left < right:
        mid = (left + right) // 2
        invc += mergesort(arr, temp, left, mid)
        invc += mergesort(arr, temp, mid + 1, right)

        invc += merge(arr, temp, left, mid, right)
    return invc


def merge(arr, temp, left, mid, right):
    i = left
    j = mid + 1
    k = left
    invc = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            invc = invc + (mid - i) + 1
            k += 1
            j += 1
    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1
    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1

    for l in range(left, right + 1):
        arr[l] = temp[l]

    return invc

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    if count(arr) == solution:
        print("Pass")
    else:
        print("Fail")

arr = [2, 5, 1, 3, 4]
solution = 4
test_case = [arr, solution]
test_function(test_case)

arr = [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
solution = 26
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 4, 2, 3, 11, 22, 99, 108, 389]
solution = 2
test_case = [arr, solution]
test_function(test_case)