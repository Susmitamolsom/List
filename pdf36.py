# list=["1","2","3","4","5","6","7","8"]
# i=0
# j=1
# a=[]
# while i<len(list):
#     b=list[i]+list[j]
#     a.append(b)
#     j=j+2
#     i=i+2
# print(a)
list=["1","2","3","4","5","6","7","8"]
i=0
a=[]
while i<len(list):
    j=i+1
    while j<len(list):
        b=list[i]+list[j]
        a.append(b)
        j=j+2
    i=i+2
print(a)