n=int(input())
x=[int(x) for x in input().split()]
big=low=x[0]
bi=li=0
for i in range(0,n):
    if(x[i]>=big):
        big=x[i]
        bi=i+1
    if(x[i]<=low):
         low=x[i]
         li=i+1
print(li,bi)
