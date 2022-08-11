#Given a List, extract all elements whose frequency is greater than K
#Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3
#Output: [4, 3]
#Explanation: Both elements occur 4 times.
#Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6], K = 2
#Output: [4, 3, 6]
#Explanation: Occur 4, 3, and 3 times respectively


#n=[4,6,4,3,3,4,3,4,6,6]
#k=2
#i=0
#list=[]
#while i<len(n):
#    j=i+1
#    sum=0
#    while j<len(n):
#        sum=sum+1
#        if n[i]==n[j] and k<=sum and n[i] not in list:
#            list.append(n[i])
#        j=j+1
#    i=i+1
#print(list)
n=[4,6,4,3,3,4,3,4,3,8]
k=3
i=0
list=[]
while i< len(n):
    j=i+1
    sum=0
    while j<len(n):
        sum=sum+1
        if n[i]==n[j] and k<=sum and n[i] not in list:
            list.append(n[i])
        j=j+1
    i=i+1
print(list)