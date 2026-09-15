nums = [10 , 20 , 30 , 40 ,  50 ]
target = 30
i=0


for i in range (len(nums)):
    if (nums[i]+nums[i+1]) ==target:
        print("Target has been found")

