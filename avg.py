L=[23,14,56,12,19,9,15,25,31,42,43]
i=0
sum=0
sum_odd=0
while i<len(L):
    if L[i]%2==0:
        sum=sum+L[i]
    else:
        sum_odd=sum_odd+L[i]
    i=i+1
total=sum
avg=total/int(len(L))
odd=sum_odd
avrg=odd/int(len(L))
print("even avg=",avg)
print("odd avg=",avrg)
