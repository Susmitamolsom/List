n=[1,1,2,3,4,5,1,2]
i=0
list=[]
while i<len(n):
    if n[i]!=1:
        list.append(n[i])
    i=i+1
print(list)