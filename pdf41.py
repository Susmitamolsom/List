#n=[[1, 2], [2, 4]]
#i=0
#while i<len(n):
#    j=0
#    while j<len(n):
#        j=j+1
#    i=i+1
#print(i,j)
#n=[[0, 1, 2], [2, 4, 5], [2, 3, 4]]
n=[[0, 1, 2], [2, 4, 5]]
i=0
while i<len(n):
    j=0
    while j<len(n[i]):
        j=j+1
    i=i+1
print(i,j)