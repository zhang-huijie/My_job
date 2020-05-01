import pandas as pd
import os
import time

time_start=time.time() #计时开始


data_path = os.getcwd()+'\data\结构化信息-0925导出.xlsx'#给出的exceL 文件
txt_to_proce_path = os.getcwd()+'\data\\excel_processed.txt'#第一次提取的出来的信息存储
txt_proced_path =  os.getcwd()+'\data\\wait_to_extract_exif.txt' #处理后的数据等待(去掉了没有序列号的)

#读取原始的excel文件
f1 = open(txt_to_proce_path,'w')
data = pd.read_excel(data_path,usecols=[1,29,39,55])
count = 0
for row in data.iterrows():
    count += 1
    a = str(row[1][0])+"--"+str(row[1][1])+"--"+str(row[1][2])+"--"+str(row[1][3])
    f1.write(a)
    f1.write('\n')
f1.closed
print("{}:{}".format('count of excel ',count))

#第一遍预处理
get_rid_of_no_imei = open(txt_to_proce_path)
all_lines = get_rid_of_no_imei.readlines()
f2 = open(txt_proced_path,'w')
count1 = 0
for line in all_lines:
    a,b,c,d = line.split('--')
    if len(c) > 4:
        count1 += 1
        f2.write(a+'--'+b+'--'+c[:15]+'--'+d)
f2.closed
print("{}:{}".format('count of excel_prcessed ',count1))

time_end = time.time()# 计时结束
print("{}:{}".format('process_time ',time_end-time_start))




