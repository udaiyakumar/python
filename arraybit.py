n=int(input())
x=[int(x) for x in input().split()]
res=x[0]
for i in range(n):
    print(x[i])
    res=res & x[i]
print(res)
