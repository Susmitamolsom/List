nums=[23,14,56,12,19,9,15,25,31,42,43]
i=0
count=0
c_even=0
c_odd=0
sum=0
sum_e=0
sum_odd=0
while i<len(nums):
    sum=sum+nums[i]
    count=count+1
    if nums[i]%2==0:
        sum_e=sum_e+nums[i]
        c_even=c_even+1
    else:
        sum_odd=sum_odd+nums[i]
        c_odd=c_odd+1
    i=i+1
avg=sum/i
avg_even=sum_e/i
avg_odd=sum_odd/i
print("count of all no.",count)
print("count of sum",sum)
print("count of even",c_even)
print("count of odd",c_odd)
print("sum of even",sum_e)
print("sum of odd",sum_odd)
print("avg of all no.",avg)
print("avg of even",avg_even)
print("avg of odd",avg_odd)