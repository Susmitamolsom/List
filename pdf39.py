n=[[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
b=[]
i=0
while i<len(n):
    c=0
    sum=0
    j=0
    while j<len(n):
        if len(n[j])>i:
            sum=sum+n[j][i]
            c=c+1
        j=j+1
    avg=sum/c
    b.append(avg)
    i=i+1
print(b)