#有n个台阶，每次可以跨一个台阶，也可以跨两个台阶，
# #走完台阶有多少种方法
def count_number(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n>2:
        return count_number(n - 1) + count_number(n - 2)
if __name__ == '__main__':
    n = 10
    print(count_number(n))



