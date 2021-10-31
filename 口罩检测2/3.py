# coding=gbk
"""
���ߣ�����
@ʱ��  : 2021/10/28 14:55
Ⱥ��970353786
"""
with open('mask.txt', 'r') as f:
    try:
        test_img_path=[]
        for line in f:
            test_img_path.append(line.strip())
    except:
        print('ͼƬ����ʧ��')

import cv2

imgs=[cv2.imread(test_img_path[1])]#��˼������ֻԤ��txt�е�һ��ͼƬ
#����ģ��
import paddlehub as hub

module = hub.Module(name="pyramidbox_lite_mobile_mask")
# module = hub.Module(name="pyramidbox_lite_server_mask")
# ���ּ��Ԥ��
visualization=True #��Ԥ��������ͼƬ���ӻ�
output_dir='detection_result' #Ԥ����ͼƬ�����ڵ�ǰ����·����detection_result�ļ�����
results = module.face_detection(images=imgs, use_multi_scale=True, shrink=0.6, visualization=True, output_dir='detection_result')
for result in results:
    print(result)

# Ԥ����չʾ
import matplotlib.image as im
import matplotlib.pyplot as plt
import os

# ��Ҫ��ȡ��·��
path_name = r'./detection_result'

for item in os.listdir(path=path_name):
    img = im.imread(os.path.join(path_name, item))
    plt.imshow(img)
    plt.show()
