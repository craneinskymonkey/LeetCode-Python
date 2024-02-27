#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2024/2/24 下午2:37
# @Author: houhaiyang
# @Project: LeetCode-Python
# @File：矩阵中块的个数.py
# @Description:
# @company：安途智驾


def count_blocks(matrix):
    """
    Leecode题目，考察深度优先搜索算法
    给出一个m * n的矩阵，矩阵中的元素为0或1。称位置（x, y）与其上下左右四个位置(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)
    是相邻的。如果矩阵中有若干个1是相邻的（不必两两相邻），那么称这些1构成了一个“块”。求给定的矩阵中“块”的个数
    :param matrix:
    :return:
    """
    def dfs(matrix, i, j, visited):
        # 检查边界条件和是否已访问
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] != 1 or visited[i][j]:
            return
            # 标记为已访问
        visited[i][j] = True
        # 递归搜索上下左右四个相邻位置
        dfs(matrix, i - 1, j, visited)
        dfs(matrix, i + 1, j, visited)
        dfs(matrix, i, j - 1, visited)
        dfs(matrix, i, j + 1, visited)
        # 搜索对角线上的相邻像素
        # dfs(matrix, i - 1, j - 1, visited)  # 左上
        # dfs(matrix, i - 1, j + 1, visited)  # 右上
        # dfs(matrix, i + 1, j - 1, visited)  # 左下
        # dfs(matrix, i + 1, j + 1, visited)  # 右下
    if not matrix or not matrix[0]:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    block_count = 0
    # 遍历整个矩阵
    for i in range(rows):
        for j in range(cols):
            # 如果当前元素为1且未被访问过，则进行DFS搜索
            if matrix[i][j] == 1 and not visited[i][j]:
                dfs(matrix, i, j, visited)
                block_count += 1
    return block_count


if __name__ == '__main__':
    # 示例用法
    matrix = [
        [0, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0],
    ]
    # result = shortest_path(matrix)
    # for row in result:
    #     print(row)
    result = count_blocks(matrix)
    print(result)
