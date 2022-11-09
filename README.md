# segment_cornerpoints
将实际分割输出数据为 lable_id x1 y1 x2 y2 x3 y3…… xn yn格式的结果通过转换，可以使用approxPolyDP函数平滑边缘，得到更少的角点。调整其中间参数值以控制滤波范围
