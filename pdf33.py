#n=[12,67,98,34]
#i=0
#while i<len(n):
#    j=0
#    b=str(n[i])
#    while j<len(b):
#        d=str(b)
#        e=0
#        c=0
#        while e<len(d):
#            c=int(d[e])+c
#            e=e+1
#        j=j+1
#    print(c,end=" ")
#    i=i+1
n=[15,81,11,234]
i=0
l=[]
while i<len(n):
    j=0
    b=str(n[i])
    while j<len(b):
        d=str(b)
        e=0
        c=0
        while e<len(d):
            c=int(d[e])+c
            e=e+1
        j=j+1
    l.append(c)
    i=i+1
print(l)