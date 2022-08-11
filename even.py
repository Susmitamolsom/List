num=[23,14,56,12,19,9,15,25,31,42,43]
i=0
sum=0
sum_odd=0
while i<len(num):
    if num[i]%2==0:
        sum=sum+num[i]
    elif num[i]%2!=0:
        sum_odd=sum_odd+num[i]
    i=i+1
print(sum)
print(sum_odd)