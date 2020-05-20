#实现最长公共前缀leecode-14
def subString(strs):
    result=strs[0]
    for i in range(1,len(strs)):
        while (strs[i].startswith(result)==False):
            result=result[0:len(result)-1]
            if len(result) == 0:
                return "无公共前缀"
    return result

#///////////////////////////////
#解法二
def longestCommonPrefix( strs):
    if not strs: return ""
    s1 = min(strs)
    s2 = max(strs)
    for i, x in enumerate(s1):
        if x != s2[i]:
            return s2[:i]
    return s1
#/////////////////////////////////
if __name__=='__main__':
    result=subString(['abc','ab','abn'])
    print (result)