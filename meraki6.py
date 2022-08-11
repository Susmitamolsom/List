name=input("enter")
i=0
while i<len(name):
    a=name[i]
    i=i+1
b=-1
c=-len(name)
while b>=c:
    d=name[b]
    b=b-1
print(d)
if a==d:
    print("palindrome")
else:
    print("not palindrome")