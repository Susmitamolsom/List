n=[[1, 2, 4], [2, 4, 4], [1, 2]]
i=0
list=[]
while i<len(n):
    j=0
    sum=0
    while j<len(n):
        if len(n[j])>i:
            a=n[j][i]
            sum=sum+a
        j=j+1
    i=i+1
    list.append(sum)
print(list)