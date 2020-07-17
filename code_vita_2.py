from collections import Counter
input()

a = input().split()
if int(a[0])>500:
    print("Number too Large")

elif a[0] == None:
    print("Invalid")
else:
    bit_list = []
    new_bit_score = 0
    for i in range(1,len(a)):


        max_1 = max(a[i])
        min_2 = min(a[i])
        bit_score = str(int(max_1)*11 + int(min_2)*7)
        if len(bit_score)==3:
            new_bit_score = bit_score[1:]
        else:
            new_bit_score = bit_score



        bit_list.append(new_bit_score)

    odd_list = []
    even_list = []
    for odd in range(0,len(bit_list),2):
        odd_list.append(bit_list[odd][0])

    for even in range(1,len(bit_list),2):
        even_list.append(bit_list[even][0])


    count_list = []
    count_list1 = []
    for i in even_list:
        d = Counter(even_list)
        count = d[i]
        count_list.append(count)
    ans = 0
    even_pair = 0

    new_list1 = list(set(count_list))
    for i in new_list1:

        if i == 1:
            even_pair = 0
        elif i == 2:
            even_pair+=1
        else:
            ans = i%2 + int(i/2)
            even_pair =ans


    ans1 = 0
    odd_pair = 0


    for i in odd_list:
        d = Counter(odd_list)
        count1 = d[i]

        count_list1.append(count1)



    new_list = list(set(count_list1))

    for i in new_list:
        if i == 1:
            odd_pair = 0
        elif i == 2:
            odd_pair+=1
        else:
            ans1 = i%2 + int(i/2)
            odd_pair = ans1

    final_pair = even_pair + odd_pair
    print(final_pair)