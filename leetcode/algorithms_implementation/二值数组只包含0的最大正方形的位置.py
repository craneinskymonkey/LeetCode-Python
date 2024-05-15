#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2024/3/8 上午11:04
# @Author: houhaiyang
# @Project: LeetCode-Python
# @File：二值数组只包含0的最大正方形的位置.py
# @Description: 给定二维数组只包含0和1，求只包含0的最大正方形的位置
#               考察点：动态规划
# @company：地平线二面

def maximalSquare(matrix):
    if not matrix:
        return 0, 0, 0

    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    max_side = 0
    max_position = (-1, -1, 0)

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if matrix[i - 1][j - 1] == '0':
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                if dp[i][j] > max_side:
                    max_side = dp[i][j]
                    max_position = (i - max_side, j - max_side, max_side)

    return max_position

if __name__ == '__main__':
    # 示例
    matrix = [
        ['1', '0', '1', '0', '0'],
        ['1', '0', '1', '0', '0'],
        ['1', '1', '1', '1', '1'],
        ['1', '0', '0', '1', '0']
    ]
    top_left_row, top_left_col, max_side = maximalSquare(matrix)
    print(f"最大正方形的左上角位置是 ({top_left_row}, {top_left_col})，边长为 {max_side}")
