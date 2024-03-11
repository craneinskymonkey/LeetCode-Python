#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2024/2/28 下午3:11
# @Author: houhaiyang
# @Project: LeetCode-Python
# @File：快速排序.py
# @Description: 快速排序是一种常用的排序算法，通过分治和递归的思想来对一个数组进行排序。你需要实现快速排序算法，对给定的数组进行升序排序。
# @company：华为OD

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2


def quicksort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quicksort(left) + middle + quicksort(right)


if __name__ == '__main__':
    arr = [3, 6, 8, 10, 1, 2, 1]
    print(quicksort(arr))
