pets=['dog','cat','fish','fish','cat']
j=input("enter")
i=0
c=0
while i<len(pets):
    if pets[i]==j:
        c=c+1
    i=i+1
print(c)
# name=["Snowfall","Chewy","Bubbles","Gruff"]
# animals=["Cat","Dog","Fish","Goat"]
# age=[1,2,2,6]
# i=0
# while i<len(name):
#     a=name[i]
#     b=animals[i]
#     c=str(age[i])
#     i=i+1
#    print(a,"the",b,"is",c)
# a=[2,4,0,5,2,0,6,0]
# i=0
# while i<len(a):
#     if a[i]==0:
#        a.append(a[i])
#        a.remove(a[i])
#     i=i+1
# print(a)