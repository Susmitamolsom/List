name="susmita"
a="a","e","i","o","u"
i=0
while i<len(name):
    if name[i] in a:
        print(name[i])
    i=i+1
    b=0
    while b<len(name):
        if name[b] not in a:
            print(name[b])
        b=b+1