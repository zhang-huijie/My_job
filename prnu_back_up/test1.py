import pandas as pd
import os
import time
import cv2
import numpy as np
import exifread

# time_start=time.time() #计时开始
# data_path = os.getcwd()+'\data\结构化信息-0925导出.xlsx'#给出的exceL 文件
# txt_to_proce_path = os.getcwd()+'\data\\excel_processed.txt'#第一次提取的出来的信息存储
# txt_proced_path =  os.getcwd()+'\data\\wait_to_extract_exif.txt' #处理后的数据等待(去掉了没有序列号的)
# exif_processed_path = os.getcwd()+'\data\\exif_processed_path.txt'#在比对完成exif后的数据信息
# exif_and_extract_exif = os.getcwd()+'\data\\exif_and_extract_exif.txt'#对比一下提取前后的是否会有不一致的情况

#处理掉一些没有imei信息的
def get_rid_of_no_imei(txt_to_proce_path):
    f1 = open(txt_to_proce_path, 'w')
    data = pd.read_excel(data_path, usecols=[1, 29, 39, 55])
    count = 0
    for row in data.iterrows():
        count += 1
        a = str(row[1][0]) + "--" + str(row[1][1]) + "--" + str(row[1][2]) + "--" + str(row[1][3])
        f1.write(a)
        f1.write('\n')
    f1.closed
    print("{}:{}".format('count of excel ', count))

    # 第一遍预处理
    get_rid_of_no_imei = open(txt_to_proce_path)
    all_lines = get_rid_of_no_imei.readlines()
    f2 = open(txt_proced_path, 'w')
    count1 = 0
    for line in all_lines:
        a, b, c, d = line.split('--')
        if len(c) > 4:
            count1 += 1
            f2.write(a + '--' + b + '--' + c[:15] + '--' + d)
    f2.closed
    print("{}:{}".format('count of excel_prcessed（get rid of no imei pic） ', count1))

#提取exif信息相同的进行存储
def extract_exif_and_process(path,exif_processed_path,exif_and_extract_exif):
    f1 = open(exif_processed_path,'w')
    f2 = open(exif_and_extract_exif,'w')
    get_rid_of_no_imei = open(path)
    all_lines = get_rid_of_no_imei.readlines()
    count_all_exif_exist = 0

    for line in all_lines:
        line = line.strip('\n')
        a, b, c, d = line.split('--')
        pic_path = os.getcwd() + '\data\\pic3\\' + d
        f = open(pic_path, 'rb')
        exif_mes = exifread.process_file(f)
        f.closed  #打开的照片路径close
        # print('Image Make' in exif_mes.keys(),'Image Model' in exif_mes.keys(),'Image Orientation' in exif_mes.keys())
        if ('Image Orientation' in exif_mes.keys()) and ('Image Make' in exif_mes.keys()):
            contrast_exif = b+'--'+str(exif_mes['Image Make'])
            f2.write(contrast_exif)#把前后对比exif存储
            f2.write('\n')
            if(str(exif_mes['Image Make']) in b):
                m = a + '--' + b + '--' + c + '--' + d
                f1.write(m)
                f1.write('\n')
                count_all_exif_exist += 1
            else:
                print('No')
    f1.closed #在比对完成exif后的数据信息
    f2.closed #给出的和提取的exif信息的所有数据
    print(count_all_exif_exist)

if __name__ == "__main__":

    time_start = time.time()  # 计时开始

    data_path = os.getcwd() + '\data\结构化信息-0925导出.xlsx'  # 给出的exceL 文件
    txt_to_proce_path = os.getcwd() + '\data\\excel_processed.txt'  # 第一次提取的出来的信息存储
    txt_proced_path = os.getcwd() + '\data\\wait_to_extract_exif.txt'  # 处理后的数据等待(去掉了没有序列号的)
    exif_processed_path = os.getcwd() + '\data\\exif_processed_path.txt'  # 在比对完成exif后的数据信息
    exif_and_extract_exif = os.getcwd() + '\data\\exif_and_extract_exif.txt'  # 对比一下提取前后的是否会有不一致的情况

    get_rid_of_no_imei(txt_to_proce_path)
    extract_exif_and_process(txt_proced_path,exif_processed_path,exif_and_extract_exif)

    time_end = time.time()  # 计时结束
    print("{}:{}".format('process_time ', time_end - time_start))