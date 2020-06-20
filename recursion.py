''' Recursion

Introduction
Recursion is a technique for solving problems where the solution to a particular problem depends on the solution to a smaller instance of the same problem.

Consider the problem of calculating  𝟸𝟻 . Let's assume to calculate this, you need to do one multiplication after another. That's  2∗2∗2∗2∗2 . We know that  25=2∗24 . If we know the value of  24 , we can easily calculate  25 .

We can use recursion to solve this problem, since the solution to the original problem ( 2𝑛 ) depends on the solution to a smaller instance ( 2𝑛−1 ) of the same problem. The recursive solution is to calculate  2∗2𝑛−1  for all n that is greater than 0. If n is 0, return 1. We'll ignore all negative numbers.

Let's look at what the recursive steps would be for calculating  25 .

25=2∗24
25=2∗2∗23
25=2∗2∗2∗22
25=2∗2∗2∗2∗21
25=2∗2∗2∗2∗2∗20
25=2∗2∗2∗2∗2∗1

'''


def power_of_2(n):
    if n == 0:
        return 1

    return 2 * power_of_2(n - 1)


print(power_of_2(5))
# print(power_of_2(10000))


def sum_integers(n):
    if n ==1:
        return 1
    else:
        return n + sum_integers(n-1)
print(sum_integers(3))

'''
Python has a limit on the depth of recursion to prevent a stack overflow. However, some compilers will turn tail-recursive functions into an iterative loop to prevent recursion from using up the stack. Since Python's compiler doesn't do this, you'll have to watch out for this limit.

Slicing
Let's look at recursion on arrays and how you can run into the problem of slicing the array. If you haven't heard the term slicing, it's the operation of taking a subset of some data. For example, the list a can be sliced using the following operation: a[start:stop]. This will return a new list from index start (inclusive) to index stop (exclusive).

Let's look at an example of a recursive function that takes the sum of all numbers in an array. For example, the array of [5, 2, 9, 11] would sum to 27 (5 + 2 + 9 + 11).'''


def sum_array(array):
    # Base Case
    if len(array) == 1:
        return array[0]

    return array[0] + sum_array(array[1:])


arr = [1, 2, 3, 4]
print(sum_array(arr))