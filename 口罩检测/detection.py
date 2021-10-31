# coding=gbk
"""
���ߣ�����
@ʱ��  : 2021/10/30 15:51
Ⱥ��970353786
"""
#���ģ���װ��
import paddlehub as hub
import cv2

def Mask_detect(image):
    state = 'δ������'
    module = hub.Module(name="pyramidbox_lite_mobile_mask")  # ����paddlehubԤѵ��ģ��
    input_dict = {"data": [image]}

    results = module.face_detection(data=input_dict)  # ���ּ��Ԥ��
    result = results[0]
    for item in result['data']:#paddlehub�Ŀ��ּ����Լ���������������ĿĬ��ÿ����Ƶ��ֻ����һ��ѧ������forѭ����ִ��һ��
        x1 = item['left']
        y1 = item['top']
        x2 = item['right']
        y2 = item['bottom']
        kz = item['label']

        image = cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, str(kz), (x1 - 5, y1 - 10), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 0, 255), 1)
        if kz == 'MASK':
            state = '�Ѵ�����'

    return image,len(result['data']),state#���ؼ��������⵽�����ĸ���������������