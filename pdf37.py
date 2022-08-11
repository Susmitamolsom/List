n=[1, 2, 3, 4, 5,6]
i=1
list=[]
while i<len(n):
    list.append([n[i]-1,n[i]])
    i=i+1
print(list)