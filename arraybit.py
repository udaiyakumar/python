n=int(input())
if(n<=100000):
    x=[int(x) for x in input().split()]
    res=x[0]
    for i in range(n):
        res=res&x[i]
    print(res)
