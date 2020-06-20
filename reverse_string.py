# Code

def reverse_string(input):
    """
    Return reversed input string

    Examples:
       reverse_string("abc") returns "cba"

    Args:
      input(str): string to be reversed

    Returns:
      a string that is the reverse of input
    """

    # TODO: Write your recursive string reverser solution here

    if len(input) == 0:
        return ""
    else:
        a = input[0]
        rest = slice(1, None)
        new = input[rest]
        reverse = reverse_string(new)
        return reverse + a


# Test Cases

print("Pass" if ("" == reverse_string("")) else "Fail")
print("Pass" if ("cba" == reverse_string("abc")) else "Fail")