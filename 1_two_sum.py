nums = [10 , 20 , 30 , 40 ,  50 ]
target = 50


for k in range ((len(nums))):
    for i in range (k+1,(len(nums))):
        if (nums[k]+nums[i]) ==target:
                print("Target has been found")

