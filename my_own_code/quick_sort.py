#春雨版本
def partition(nums, l, r):
	v = nums[l]
	left = l + 1
	right = r - 1
	while True:
		while left < r and nums[left] < v:
			left += 1
			if left >= r:
				break
		while right >= l and nums[right] > v:
			right -= 1
			if right <= l:
				break
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
		qsort(nums, l, mid)
		qsort(nums, mid+1, r)

if __name__ == "__main__":
	nums = [1,3,4,5,2,6,9,7,8,0]
	qsort(nums, 0, len(nums))
	print(nums)






