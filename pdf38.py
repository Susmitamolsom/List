list=['.com', '.edu', '.tv']
str='https://www.w3resource.com/python-exercises/list/'
i=0
while i<len(list):
    if list[i] in str:
        print("true")
        break
    else:
        print("false")
    i=i+1