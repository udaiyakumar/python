n=int(input())
x=[int(x) for x in input().split()]
for i in range(0,n-1,2):
    temp=x[i]
    x[i]=x[i+1]
    x[i+1]=temp
for i in range(n):
    print(x[i],end=' ')
