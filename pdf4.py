list=[6,1,3,5,6,3,1]
i=0
b=[]
while i<len(list):
    if list[i] not in b:
        b.append(list[i])
    i=i+1
j=0
prod=1
while j<len(b):
    prod=prod*b[j]
    j=j+1
print(prod)