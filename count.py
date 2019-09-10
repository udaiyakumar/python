n,k=input().split()
x=[int(x) for x in input().split()]
count=0
for i in range(int(n)):
  if(int(k)==x[i]):
      count+=1
print(count)
  
