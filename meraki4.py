list=[50,40,23,70,56,12,5,10,7]
maxv=list[0]
i=0
while i<len(list):
    if maxv<list[i-1]:
        maxv=list[i]
    i=i+1
print(maxv)