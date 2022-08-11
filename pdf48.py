n=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
i=0
list=[]
a=int(input("enter"))
while i<len(n):
    list.append(n[i:i+a])
    i=i+a
print(list)