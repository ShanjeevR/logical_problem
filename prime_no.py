a=7
sum=0
for i in range(2,a//2):
    if a%i==0:
        sum=sum+1
if sum==0:
    print("its a prime number")
else:
    print("not a prime number")            
