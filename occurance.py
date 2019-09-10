n=int(input())
l,r=input().split()
count=0
for i in range(int(l),int(r)):
  if(i==n):
    count+=1
if(count==1):
  print('yes')
else:
  print('no')
