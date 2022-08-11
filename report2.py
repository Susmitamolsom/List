L=[[78,76,94,86,88],[91,71,98,65],[95,45,78]]
i=0
sum=0
while i<len(L):
    j=0
    while j<len(L[i]):
        k=L[i][j]
        sum=sum+k
        j=j+1
    i=i+1
print(sum)