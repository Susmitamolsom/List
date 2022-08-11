marks=[
    [78,76,94,86,88],
    [91,71,98,65,76],
    [95,45,78,52,49]
]
i=0
total_marks=0
while i<len(marks):
    j=0
    while j<len(marks[i]):
        total_marks=total_marks+marks[i][j]
        j=j+1
    i=i+1
print(total_marks)