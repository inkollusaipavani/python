p,q=map(int,raw_input().split())
if(p>q):
    min1=p
else:
    min1=q
while(1):
    if(min1%n==0 and min1%m==0):
        print(min1)
        break
    min1=min1+1
