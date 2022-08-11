#13.#Write a Python program to create a list reflecting the modified run-length encoding from
#a given list of integers or a given list of characters.
#Original list:
#[1, 1, 2, 3, 4, 4, 5, 1]
#List reflecting the modified run-length encoding from the said list:
#[[2, 1], 2, 3, [2, 4], 5, 1]
#Original String:
#aabcddddadnss
#List reflecting the modified run-length encoding from the said string:
#[[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]
n=[1, 1, 2, 3, 4, 4, 5, 1]
i=0
list=[]
while i<len(n):
    k=n[i]
    count=0
    while (i<len(n) and n[i]==k):
        count=count+1
        i=i+1
    if count>1:
        list.append([count,k])
    else:
        list.append(k)
print(list)