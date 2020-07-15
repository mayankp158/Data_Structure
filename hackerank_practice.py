grades = [59,36,97,28,61,54,27,14,29,81,16,7,1,99,42,77,39,20,29,0,1,82,20,71,71,73,79,77,61,7,93,36,65,11,92,87,85,62,45,33,9,6,37,31,67,32,67,73,59,95]
# n1 = 37
# n2 = n1

def gradingStudents(grades):
    ans = []
    # Write your code here
    for a1 in grades:
        a2 = a1
        if (a2 < 38 or a2==0) or (a2 % 5 == 0 and a2!=0):
            ans.append(a2)
        while (a2 % 5 != 0 and a1 >= 38):
            a2 = a2 + 1
            if a2 % 5 == 0 and a2 - a1 < 3:
                ans.append(a2)
            else:
                if a2 % 5 == 0 and (a2 - a1 >= 3):
                    ans.append(a1)

    print(ans)

gradingStudents(grades)