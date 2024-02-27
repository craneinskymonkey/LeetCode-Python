#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2024/2/24 下午2:45
# @Author: houhaiyang
# @Project: LeetCode-Python
# @File：矩阵旋转.py
# @Description:
# @company： 零跑汽车



def rotate(matrix):
    '''
    领跑面试题目
    :param matrix:
    :return:
    '''
    n = len(matrix)
    # Step 1: 转置矩阵
    for i in range(n):
       for j in range(i+1, n):
           matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: 反转每一行
    for i in range(n):
       matrix[i].reverse()

# 示例用法
matrix = [
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]
]

rotate(matrix)
print(matrix)

if __name__ == '__main__':
    pass
