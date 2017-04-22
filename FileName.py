# -*- coding: utf-8 -*-
import os;
file_folder=r"D:\小论文相关资料\遥感数据";#根据需要遍历的文件名字输入文件夹的名字
upath=unicode(file_folder,'utf-8')
print(upath)
list1=os.listdir(upath)
print (len(list1))
file = open('data1.txt','w')
for i in list1:
    file.write(r'./data/'+i+'\n')
file.close();
