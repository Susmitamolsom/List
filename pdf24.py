n=[1,2,3,1,2,2]
i=0
list=[]
while i<len(n):
    if n[i] not in list:
        list.append(n[i])
    i=i+1
print(list)