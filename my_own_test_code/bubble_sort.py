# 实现冒泡排序
def bubble_sort(arry):
    for i in range(0, len(arry) - 1):
        for j in range(0, len(arry) - 1 - i):
            if arry[j] > arry[j + 1]:
                arry[j], arry[j + 1] = arry[j + 1], arry[j]
    return arry


if __name__ == '__main__':
    a = [1, 2, 3, 4, 7, 6, 5]
    print(bubble_sort(a))

