inp = []
t = int(input())
for i in range(t):
    k = int(input())
    inp.append(k)

def fib(n):
    if n == 0 or n==1:
        print('0')
        print(end='\n')
    elif n==2:
        for i in range(0,n):
            print(i,end=' ')
        print(end='\n')
    else:
        bottom_up = [0] * (n+1)
        bottom_up[1] = 0
        bottom_up[2] = 1
        for i in range(3,n+1):
            bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
        for i in range(n):
            print(bottom_up[i+1],end=' ')
        print(end='\n')

for n in inp:
    answer = fib(n)