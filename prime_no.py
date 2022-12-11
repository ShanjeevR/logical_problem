a=5
sum=0
for i in range(2,a//2):
    if a%i==0:
        sum=sum+1
if sum==0:
    print("prime number")
else:
    print("Not a prime number")            
