a=int(input('enter number'))
sum=0
while a<=50:
    i=2
    while i<=a//2:
        if a%i==0:  
            break              
        i=i+1
    else:
        sum=sum+1
        print(a,'is prime number')
    if sum==5:
        break
    a=a+1