list=[50,40,23,70,56,12,5,10,7]
i=0
c=0
while i<len(list):
    if list[i]>20 and list[i]<40:
        c=c+1
    else:
        pass
    i=i+1
print(c)