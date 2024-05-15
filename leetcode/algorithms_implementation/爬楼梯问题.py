#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2024/3/6 下午11:28
# @Author: houhaiyang
# @Project: LeetCode-Python
# @File：爬楼梯问题.py
# @Description:
# @company：

def climbStairs(n: int) -> int:
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

if __name__ == '__main__':
    n = climbStairs(4)
    print(n)
