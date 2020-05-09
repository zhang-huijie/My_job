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
'''
#leecode上面题目解决方法，空间开销代替时间开销
def solution(nums,target):
	#新建立一个空字典用来保存数值及其在列表中对应的索引
	dict1 = {}
	#遍历一遍列表对应的时间复杂度为O(n)
        for i in range(0, len(nums)):
            #相减得到另一个数值
            num = target - nums[i]
            #如果另一个数值不在字典中，则将第一个数值及其的索引报错在字典中
            #因为在字典中查找的时间复杂度为O(1)，因此总时间复杂度为O(n)
            if num not in dict1:
                dict1[nums[i]] = i
            #如果在字典中则返回
            else:
                return [dict1[num], i]
'''
