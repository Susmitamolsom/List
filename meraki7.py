bin=[1,1,0,1,1,0,0,1]
i=0
dec=0
while i<len(bin):
    if bin[i]==1:
        dec=dec+2**i
    i=i+1
print(dec)