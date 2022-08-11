n=[2,3,9,8,2,0,39,84,22,34,2,34,5,3,5]
i=0
b=[]
list=int(input("enter"))
while i<len(n):
    p=n[i:list]
    b.append(p)
    i=i+1
    break
print(b)