#自己的修改后版本
def partition(nums, l, r):
	v = nums[l]
	left = l+1
	right = r
	while True:
		while left <= r and nums[left] < v:
			left += 1
		while right >= l and nums[right] > v:
			right -= 1
		if left >= right:
			break
		nums[left], nums[right] = nums[right], nums[left]
	nums[l], nums[right] = nums[right], nums[l]
	return right
def qsort(nums, l, r):
	if l >= r:
		return nums
	else:
		mid = partition(nums, l, r)
		qsort(nums, l, mid-1)
		qsort(nums, mid+1, r)

#//////////////////////////////////////////////////////////////
# 空间开销比较大的另一种方式
def quick_sort(seq):
    if(len(seq) < 2):
        return seq
    else:
        base = seq[0]
        left = [elem for elem in seq[1:] if elem < base]
        right = [elem for elem in seq[1:] if elem > base]
        return quick_sort(left) + [base] + quick_sort(right)
#//////////////////////////////////////////////////////////////
#迷惑解法3
def quicksort(data):     #快速排序
    stone = data[0]
    i = 1
    j = len(data)-1
    if len(data) > 1:     #分为len(data) >2和len(data) == 2两种情况，可合并
        while j > i:
            if data[j] <= stone:
                if data[i] > stone:
                    data[j], data[i] = data[i], data[j]
                else:
                    i += 1
            else:
                j -= 1
        if data[j] <= stone:     #当len(data) == 2时只执行此部分
            data[0], data[j] = data[j], data[0]
        return quicksort(data[:j]) + quicksort(data[j:])
    else:     #回归条件，len(data) <= 1
        return data

if __name__ == "__main__":
	nums = [1,3,4,5,2]
	print(quicksort(nums))





