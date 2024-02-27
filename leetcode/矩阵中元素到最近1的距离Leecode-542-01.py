#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2024/2/24 下午2:05
# @Author: houhaiyang
# @Project: LeetCode-Python
# @File：矩阵中元素到最近1的距离Leecode-542-01.py
# @Description: 给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。两个相邻元素间的距离为 1 。
# @company: 小红书


from typing import List
import collections
from collections import deque


def shortest_path(matrix):
    """
    百度文心一言给出的结果
    小红书面试题目，考点：广度优先搜索
    给定一个N*M的二维矩阵，矩阵中元素为0或1，计算矩阵中元素到达最近的1的步长（只能上下左右行走，元素为1的位置步长为0），最终输出一个N*M的最短步长结果矩阵
    :param matrix:
    :return:matrix
    """
    # 百度文心一言生成结果
    if not matrix or not matrix[0]:
        return []

    n, m = len(matrix), len(matrix[0])  # n行，m列
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 右，左，下，上
    queue = deque()
    res = [[float('inf')] * m for _ in range(n)]  # 初始化结果矩阵为无穷大

    # 将所有值为1的元素的位置和步长加入队列，并将对应的结果矩阵位置设为0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                queue.append(((i, j), 0))
                res[i][j] = 0

    # 广度优先搜索
    while queue:
        pos, step = queue.popleft()
        x, y = pos
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and res[nx][ny] == float('inf'):
                res[nx][ny] = step + 1
                queue.append(((nx, ny), step + 1))
    return res


class Solution:
    # 官方题解
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        dist = [[0] * n for _ in range(m)]
        zeroes_pos = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 1]
        # 将所有的 1 添加进初始队列中
        q = collections.deque(zeroes_pos)
        seen = set(zeroes_pos)

        # 广度优先搜索
        while q:
            i, j = q.popleft()
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))
                    seen.add((ni, nj))

        return dist


if __name__ == '__main__':
    matrix = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    ret = shortest_path(matrix)
    print(ret)