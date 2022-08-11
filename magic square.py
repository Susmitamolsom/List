num=[[8,3,4],
     [1,5,9],
     [6,7,2]]
sum=0
sum2=0
sum3=0
i=0
while i<len(num):
    sum=num[i][0]+sum
    sum2=sum2+num[i][1]
    sum3=sum3+num[i][2]
    j=0
    sum1=0
    while j<len(num):
        sum1=sum1+num[j][j]
        j=j+1
    i=i+1
    print(sum1)
print(sum)
print(sum2)
print(sum3)
d=0
f=0
dig=0
while d<len(num):
    while f<len(num[d]):
        if d==f:
           k=num[d][f]
           dig=dig+k
           break
        f=f+1
    d=d+1
print(dig)
g=0
h=0
dig2=0
while g<len(num):
    while h<len(num[g]):
        if g==h:
           c2=num[g][h]
           dig2=dig2+c2
           break
        h=h+1
    g=g+1
print(dig2)
if sum==sum2==sum3==sum1 and dig==dig2:
    print("it is a magic square")
else:
    print("its not magic square")