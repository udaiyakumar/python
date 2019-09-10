n=int(input())
res=0
if(n<=100000):
    x=[int(x) for x in input().split()]
    for i in range(n):
        res=res|x[i]
print(res)
