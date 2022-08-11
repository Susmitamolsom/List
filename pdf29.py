n=[5,6,[],3,[],[],9]
i=0
list=[]
while i<len(n):
    if n[i]!=[]:
        list.append(n[i])
    i=i+1
print(list)