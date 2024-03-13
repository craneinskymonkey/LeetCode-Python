#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2024/3/11 下午9:09
# @Author: houhaiyang
# @Project: LeetCode-Python
# @File：iou计算.py
# @Description:
# @company：
def bbox_iou(box1, box2):
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])
    inter_area = max(x2-x1+1, 0)*max(y2-y1+1, 0)
    box1_area = (box1[2]-box1[0]+1)*(box1[3]-box1[1]+1)
    box2_area = (box2[2]-box2[0]+1)*(box2[3]-box2[1]+1)
    uniou_area = box1_area+box2_area-inter_area
    iou = inter_area/uniou_area
    return iou

if __name__ == '__main__':
    box1 = [0, 0, 5, 5]
    box2 = [2, 2, 7, 7]
    ret = bbox_iou(box1, box2)
    print(ret)
