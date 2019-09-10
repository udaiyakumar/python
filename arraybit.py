n=int(input())
res=1
x=[int(x) for x in input().split()]
for i in range(n):
    res=res&x[i]
print(res)
