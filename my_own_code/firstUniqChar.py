#找到第一个出现的不重复的leecode-50
#我写的和别人写的
def firstUniqChar(s):
    m = [" "]
    count = 0
    if len(s) < 1:
        return " "
    else:
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                m = s[i]
                return m
                break
            elif i == len(s) - 1:
                return " "

#////////////////////////////////
#别人写的
class Solution:
    def firstUniqChar(self, s: str) -> str:
        while len(s)>0:
            e=s[0]
            if s.count(e)>1:
                s=s.replace(e,"")
            else:
                return e
        return " "
#解答方法3
class Solution_1:
    def firstUniqChar(self, s: str) -> str:
        if not s:
            return " "
        dp={}
        for i in s:
            if i not in dp:
                if s.count(i)!=1:
                    dp[i]=1
                else:
                    return i
        return " "

if __name__ == '__main__':
    s = "abaccdeff"
    print(firstUniqChar(s))
    a = Solution()
    a.firstUniqChar(s)