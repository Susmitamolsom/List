n=[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
k=[[61], [12, 14, 15], [12, 13, 19, 20], [12]]
i=0
list=[]
while i<len(n):
    a=n[i]+k[i]
    list.append(a)
    i=i+1
print(list)