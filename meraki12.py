list1=["a","b","a","c","b","e"]
list2=[]
i=0
while i<len(list1):
    if list1[i] not in list2:
        list2.append(list1[i])
    i=i+1
print(list2)