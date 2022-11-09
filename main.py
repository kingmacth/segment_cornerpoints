import cv2
import numpy as np
import matplotlib.pyplot as plt
#point_list 为实例分割输出检测结果，数据为 lable_id x1 y1 x2 y2 x3 y3…… xn yn格式
def list2cornerpoins(point_list):
  for box_data in point_list:
    points = []
    box_data = box_data.split()
    if len(box_data) > 0:
        l1 = [i for i in box_data[1:]]
        for i in range(0, len(l1), 2):
            point_data = l1[i:i + 2]
            point_data[0] = int(point_data[0])
            point_data[1] = int(point_data[1])
            points.append(point_data)
        points_mat = np.mat(np.array(points))           #将list数据转化为approxPolyDpj接受的输入数据
        approx = cv2.approxPolyDP(points_mat, 10, True)  #调整值的大小，可以调整平滑度
        cv2.drawContours(cv_img, [approx], 0, (144, 238, 144), 5)
    
