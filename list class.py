# num=[1,1,2,2,3,5,5,7]
# n=[]
# for i in range(0,len(num)):
#     c=0
#     a=num[i]
#     for j in range(0,len(num)):
#         if a==num[j]:
#             c=c+1
#     if c==1:
#         n.append(a)
# print(n)



ch="welcome 35 to navgurukul 2016"
list1=ch.split( )
print(list1)
list2=[]
i=0
while i<len(list1):
    if list1[i].isalpha():
        list2.append(list1[i])
    i=i+1
print(list2)