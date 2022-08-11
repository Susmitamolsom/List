list=[50,40,23,70,56,12,5,10,7]
i=0
list1=0
while i<len(list):
    if list[i]>list1:
        list1=list[i]
    i=i+1
print(list1)