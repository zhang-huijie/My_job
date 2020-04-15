import sys 

# 判断是否是合法输入
def x(ls):
    for name in ls:
        if 'A'<= name[0] <= 'Z':
            pass
        else:
            print('error.0001')
            return;
        left_name = name[1:]
        if left_name == '':
            print('error.0001')
            return;
        for s in left_name:
            if 'a' <= s <= 'z':
                pass
            else:
                print('error.0001')
                return;
    dic = {}
    for name in ls:
        dic[name] = dic.get(name,0) + 1
    # items = list(dic.items())
    # items.sort(key=lambda x:x[1], reverse=True)
    # print(items[0][0])
    mcount = 0
    mname = ''
    for name,count in dic.items():
        if count > mcount:
            mcount = count
            mname = name
        elif count == mcount:
            length = min(len(name),len(mname))
            i = 0
            while(i<length):
                if name[i] < mname[i]:
                    mname = name
                    break
                elif name[i] > mname[i]:
                    break                
                i = i + 1
            if i==length:
                if len(name)<len(mname):
                    mname = name
    print(mname)
if __name__ == "__main__":
    ls = list(sys.stdin.readline().strip().split(','))
    x(ls)