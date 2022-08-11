str_char=["a","b","c","d","e","f","g","h"]
i=0
k=3
list=[]
while i<len(str_char):
    if str_char[i] not in list:
        list.append(str_char[k%len(str_char)])
        k=k+1
    i=i+1
print("the cycle list is:",list)