#剑指offer-面试题62
#采用倒推的方法,约瑟夫环
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        index_tmp = 0
        for i in range(2,n+1):
            index_tmp = (index_tmp + m) % i
        return index_tmp

if __name__ == '__main__':
    a = Solution()
    print(a.lastRemaining(5,3))


