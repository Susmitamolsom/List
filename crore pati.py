num=[3000,6000000,324990909,90990900,30000,5600000,690909090,31010101,532010,510,4100]
i=0
cp=0
lp=0
dl=0
while i<len(num):
    if num[i]>10000000:
        cp=cp+1
    elif num[i]>100000:
        lp=lp+1
    else:
        dl=dl+1
    i=i+1
print("crorepati=",cp)
print("lakhpati=",lp)
print("dilwale=",dl)