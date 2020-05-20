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



if __name__ == "__main__":
	nums = [4,3,2,5,1]
	qsort(nums, 0, len(nums)-1)
	print(nums)





