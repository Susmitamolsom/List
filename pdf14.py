a=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
i=0
max=[0]
min=[0]
while i<len(a):
    if a[i]<max:
        min=a[i]
    else: 
        min=a[i]
    i=i+1
b=len(min),min
d=len(max),max
print(b)
print(d)