n=[1234, 122, 1984, 19372, 100]
#n=[1234, 922, 1984, 19372, 100]
i=0
while i<len(n):
    a=str(n[i])
    b=str(n[i])
    if a[0]+b[0]==1:
        match=True 
    else:
        match=False
    i=i+1
print(match)