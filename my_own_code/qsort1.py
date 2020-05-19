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

if __name__ == "__main__":
	nums = [4,3,2,5,1]
	qsort(nums, 0, len(nums)-1)
	print(nums)






