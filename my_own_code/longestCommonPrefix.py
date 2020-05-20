#实现最长公共前缀
def subString(strs):
    result=strs[0]
    for i in range(1,len(strs)):
        while (strs[i].startswith(result)==False):
            result=result[0:len(result)-1]
            if len(result)==0:
                return "无公共前缀"
    return result
if __name__=='__main__':
    result=subString(['abc','ab','abn'])
    print (result)