# coding=gbk
"""
���ߣ�����
@ʱ��  : 2021/10/28 14:42
Ⱥ��970353786
"""
# ��Ԥ��ͼƬ
test_img_path = ["./0.png"]

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread(test_img_path[0])

# չʾ��Ԥ��ͼƬ
plt.figure(figsize=(10,10))
plt.imshow(img)
plt.axis('off')
plt.show()
