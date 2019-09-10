a=input()
upr=0
lwr=0
for i in range(len(a)):
    if(ord(a[i])<=122 and ord(a[i])>=97):
        lwr+=1
    elif(ord(a[i])<=90 and ord(a[i])>=65):
        upr+=1
print(lwr)
print(upr)
