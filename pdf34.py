n=[34.67, 12, -94.89, 'Python', 0, 'C#']
i=0
list=[]
while i<len(n):
    if type(n[i])==int:
        list.append(n[i])
    i=i+1
print(list)