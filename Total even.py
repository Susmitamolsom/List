L=[23,14,56,12,19,9,15,25,31,42,43]
i=0
e=[]
o=[]
while i<len(L):
    if L[i]%2==0:
        e.append(L[i])
    elif L[i]%2!=0:
        o.append(L[i])
    i=i+1
print(e)
print(o)