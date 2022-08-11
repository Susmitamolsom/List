n=[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
a=20
b=4
i=b
while i<len(n):
    n.insert(i,a)
    i=i+b+1
print(n)