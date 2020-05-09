#python 实现二分查找、
def binary_chop(alist,data):
    #递归解决二分查找
    n = len(alist)
    if n<1:
        return False
    mid = n//2
    if alist[mid]>data:
        return binary_chop(alist[0:mid],data)
    elif alist[mid]<data:
        return binary_chop(alist[mid+1:], data)
    else:
        return True

def binary_chop_1(alist, data):
    """
    非递归解决二分查找
    """
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (last + first) // 2
        if alist[mid] > data:
            last = mid - 1
        elif alist[mid] < data:
            first = mid + 1
        else:
            return mid
    return False


if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,8]
    print(binary_chop_1(a,7))
    print(binary_chop(a,7))
