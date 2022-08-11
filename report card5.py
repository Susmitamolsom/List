n=[[78,76,94,86,88],[91,71,98,65],[95,45,78]]
i=0
year=1
while i<len(n):
    j=0
    sum=0
    while j<len(n[i]):
        k=n[i][j]
        sum=sum+k
        j=j+1
    b=sum//len(n[i])
    print("avg of",year,"year=",b)
    i=i+1
    year=year+1