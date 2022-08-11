char_list=["a","n","t","a","a","t","n","n","a","x","u","g","a","x","a"]
b=97
c=122
i=[]
while b<=c:
    a=0
    sum=0
    k=[]
    while a<len(char_list):
        if char_list[a]==chr(b):
            e=char_list[a]
            sum=sum+1
        a=a+1
    if sum>0:
        k.append(e)
        k.append(sum)
        i.append(k)
    b=b+1
print(i)