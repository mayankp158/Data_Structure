# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#     arr = []
#     for a in range(0,x+1):
#         for b in range(0,y+1):
#             for c in range(0,z+1):
#                 d = a+b+c
#                 if(d!=n):
#                     arr.append([a,b,c])
#     print(arr)
#
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     b = max(arr)
#     arr2 = []
#     for a in arr:
#         if (a<b):
#             arr2.append(a)
#     print(max(arr2))
#
# if __name__ == '__main__':
#     a = []
#     c = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#
#         b = []
#         b.append(name)
#         b.append(score)
#         a.append(b)
#         c.append(score)
#     score_uniq_list = list(set(c))
#     score_uniq_list.sort()
#     print(score_uniq_list)
#     for e,f in sorted(a):
#         if f == score_uniq_list[1]:
#             print(e)
#
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     sum_n = 0
#     avg = 0
#     i = 0
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#
#     for a in student_marks:
#         if a == query_name:
#             marks = student_marks[a]
#             for b in marks:
#                 sum_n += b
#                 i +=1
#             avg = sum_n/i
#             two_decimal_place = "{:.2f}".format(avg)
#             print(two_decimal_place)