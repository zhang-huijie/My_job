import cv2
import numpy as np
import os
import pandas as pd
import exifread

txt_proced_path =  os.getcwd()+'\data\\all_process.txt'#在提取exif之前的东西
exif_rocessed_path = os.getcwd()+'\data\\exif_data.txt'#在比对完成exif后的数据信息
exif_and_extract_exif = os.getcwd()+'\data\\exif_and_extract_exif.txt'#对比一下提取前后的是否会有不一致的情况

#提取exif信息相同的进行存储
def extract_exif_and_process(path,exif_rocessed_path,exif_and_extract_exif):
    f1 = open(exif_rocessed_path,'w')
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
        # print('Image Make' in exif_mes.keys(),'Image Model' in exif_mes.keys(),'Image Orientation' in exif_mes.keys())
        if ('Image Orientation' in exif_mes.keys()) and ('Image Make' in exif_mes.keys()):
            contrast_exif = b+'--'+str(exif_mes['Image Make'])
            f2.write(contrast_exif)
            f2.write('\n')
            if(str(exif_mes['Image Make']) in b):
               pass
            else:
                print('No')
            count_all_exif_exist += 1
            m = a+'--'+b+'--'+c+'--'+d
            f1.write(m)
            f1.write('\n')
    f.closed
    f1.closed
    f2.closed
    print(count_all_exif_exist)
    # f1.closed
extract_exif_and_process(txt_proced_path,exif_rocessed_path,exif_and_extract_exif)

