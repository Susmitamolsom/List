# a=[1,2,3]
# b=["one","two","three"]
# i=0
# l=[]
# while i<len(a):
#     c=a[i]
#     d=b[i]
#     l.append(c)
#     l.append(d)
#     i=i+1
# print(l)
a=[[5,3,10],[1,8,9],[6,4,2]]
i=0
while i<len(a):
    j=0
    sum=0
    while j<len(a[i]):
        sum=sum+a[i][j]
        j=j+1
    i=i+1
print("row",sum)
print("cloum",sum)