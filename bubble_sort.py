wakeup_times = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]
def bubble_sort_1(l):

    for a in range(len(l)):
        for i in range(1,len(l)):
            this = l[i]
            prev = l[i-1]
            if prev<this:
                continue
            l[i-1] = this
            l[i] = prev
bubble_sort_1(wakeup_times)
print ("Pass" if (wakeup_times[0] == 3) else "Fail")

# Entries are (h, m) where h is the hour and m is the minute
sleep_times = [(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)]

def bubble_sort_2(l):

    for a in range(len(l)):
        for i in range(1,len(l)):
            this1,this2 = l[i]
            prev1,prev2 = l[i-1]
            if (this1,this2) < (prev1,prev2):
                continue
            l[i-1] = this1,this2
            l[i] = prev1,prev2

bubble_sort_2(sleep_times)
print ("Pass" if (sleep_times == [(24,23), (24,13), (24,3), (23,20), (22,5), (21,58), (21,55)]) else "Fail")