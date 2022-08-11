n=["0","1","2","3","4"]
colours=["red","green","black","blue","black"]
num=["100","200","300","400","500"]
i=0
c=[]
while i<len(n):
    b=n[i]+colours[i]+num[i]
    c.append(b)
    i=i+1
print(c)