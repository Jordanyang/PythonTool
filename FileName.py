# -*- coding: utf-8 -*-
import os;
file_folder=r"D:\С�����������\ң������";#������Ҫ�������ļ����������ļ��е�����
upath=unicode(file_folder,'utf-8')
print(upath)
list1=os.listdir(upath)
print (len(list1))
file = open('data1.txt','w')
for i in list1:
    file.write(r'./data/'+i+'\n')
file.close();
