a=input("enter")
rev=0-len(a)
i=-1
sum=""
while i>=rev:
    sum=sum+a[i]
    i=i-1
if int(a)==int(sum):
    print("true")
else:
    print("false")