#给定一个整数数组 nums 和一个目标值 target，
# 请你在该数组中找出和为目标值的那 两个 整数，
# 并返回他们的数组下标。你可以假设每种输入只会对应一个答案。
# 但是，你不能重复利用这个数组中同样的元素。
nums = list(map(int,input().rstrip().split()))
target = int(input())
tag = [1 for i in range(len(nums))]
for i in range(0,len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            if tag[i] == 1 and tag[j] == 1:
                print(i,j)
                tag[i],tag[j] = 0,0
            else:
                continue


