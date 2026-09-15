nums = [10 , 20 , 30 , 40 ,  50 ]
target = 40
i=0



for i in range ((len(nums)) - 1):
    j=i+1
    if (nums[i]+nums[j]) ==target:
        print("Target has been found")

