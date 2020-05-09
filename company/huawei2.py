import sys

def Match(X,item):
    ls = item.split('[')
    first = ls[0]
    second = ls[1]
    if first != X:
        # print("FALT")
        return;
    content = second.split(',')
    if len(content) != 3:
        print("FALT")
        return;
    # 提取三项内容
    if (content[0][:7] == "addr=0X" or content[0][:7] == "addr=0x") == False:
        print("FALT")
        return;
    if (content[1][:7] == "mask=0X" or content[1][:7] == "mask=0x") == False:
        print("FALT")
        return;
    if (content[2][:6] == "val=0X" or content[2][:6] == "val=0x") == False:
        print("FALT")
        return;
    print(content[0][5:]+ ' ' + content[1][5:]+ ' ' + content[2][4:])

if __name__ == "__main__":
    ls = list(sys.stdin.readline().strip().split(' '))
    X = ls[0]
    ls = ls[1].split('],')
    for item in ls:
        if item == ls[-1]:
            if item[-1] == ']':
                Match(X,item[:-1])
            else:
                print('FALT')
        else:
            Match(X,item)