#输入型号的string类型转变成输出的二维数组

matrix =input()
arr = int(matrix.count(']')-1)
matrix = matrix.split(',')
res = []

for i in range(len(matrix)):
    m = matrix[i]
    s = ""
    for j in range(len(m)):
        if m[j] ==']' or m[j] =='[':
            continue
        else:
            s = s+str(m[j])   
    res.append(int(s))
cut_count = int(len(res)/arr)

result = [[0] * cut_count for i in range(arr)]
count = 0
for i in range(0,arr):
    for j in range(0,cut_count):
        result[i][j] = res[count]
        count += 1
print(result)





    
        
        

            



    





