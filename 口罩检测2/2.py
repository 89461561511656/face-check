# coding=gbk
"""
���ߣ�����
@ʱ��  : 2021/10/28 14:45
Ⱥ��970353786
"""
with open('mask.txt', 'r') as f:
    try:
        test_img_path=[]
        for line in f:
            test_img_path.append(line.strip())
    except:
        print('ͼƬ����ʧ��')
print(test_img_path)
