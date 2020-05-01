import cv2
import numpy as np
import os
import pandas as pd
import exifread

txt_proced_path =  os.getcwd()+'\data\\wait_to_extract_exif.txt' #处理后的数据等待
exif_processed_path = os.getcwd()+'\data\\exif_processed_path.txt'#在比对完成exif后的数据信息
exif_and_extract_exif = os.getcwd()+'\data\\exif_and_extract_exif.txt'#对比一下提取前后的是否会有不一致的情况

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
extract_exif_and_process(txt_proced_path,exif_processed_path,exif_and_extract_exif)

