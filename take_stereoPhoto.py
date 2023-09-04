#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2

outputpath_L = "img/LEFT/"
outputpath_R = "img/RIGHT/"

cap = cv2.VideoCapture(1)
count = 0

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # 读取当前帧
    ret, frame = cap.read()
    crop_frame_L = frame[:,:640]
    crop_frame_R = frame[:,640:]
    
    # 显示当前帧
    cv2.imshow("Camera", frame)

    # 检查是否按下 "G" 键
    key = cv2.waitKey(1) & 0xFF
    if key == ord('g'):
        # 生成文件名
        filenameL = outputpath_L + "L_" + str(count) +".JPG"
        filenameR = outputpath_R + "R_" + str(count) +".JPG"
        count += 1
        # 保存图像
        cv2.imwrite(filenameL, crop_frame_L)
        cv2.imwrite(filenameR, crop_frame_R)
        print(f"图像已保存为 {filenameL}")
        print(f"图像已保存为 {filenameR}")

    # 检查是否按下 "q" 键来退出循环
    if key == ord('q'):
        break

# 释放相机资源
cap.release()
cv2.destroyAllWindows()