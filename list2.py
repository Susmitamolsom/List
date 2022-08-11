
list1=[1,2,2,4,1,2,5,3]
list2=[]
l1=[]
i=0
while i<len(list1):
    if list1[i] not in list2:
        list2.append(list1[i])
    i=i+1
j=0
while j<len(list2):
    list3=list()
    a=list1.count(list2[j])
    if a>1:
        list3.append(list2[j])
        l1.append(list3)
    else:
        l1.append(list2[j])
    j=j+1
print(l1)