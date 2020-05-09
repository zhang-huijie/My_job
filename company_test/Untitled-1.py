def bina_chack(arry,data):
    if len(arry)<1:
        return False

    mid = len(arry)//2
    if data<arry[mid]:
        return bina_chack(arry[0:mid],data)
    elif data>arry[mid]: 
        return bina_chack(arry[mid+1:],data)
    else:
        return True
if __name__ == '__main__':
    a = [1,2,3,4,5,6]
    print(bina_chack(a,4))

    