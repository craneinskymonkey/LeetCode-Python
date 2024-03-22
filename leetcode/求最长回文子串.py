#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2024/3/17 下午3:04
# @Author: houhaiyang
# @Project: LeetCode-Python
# @File：求最长回文子串.py
# @Description: 最长回文子串
# @company：拼多多


def longest_palindrome(s):
    n = len(s)
    if n < 2:
        return s

        # 创建一个二维数组来存储子问题的解
    # dp[i][j] 表示从索引 i 到 j 的子串是否是回文串
    dp = [[False] * n for _ in range(n)]
    max_len = 1
    start = 0

    # 初始化单个字符的回文串
    for i in range(n):
        dp[i][i] = True

        # 检查所有长度为2的子串
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            max_len = 2
            start = i

            # 检查所有长度大于2的子串
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_len:
                    max_len = length
                    start = i

                    # 返回最长回文子串
    return s[start:start + max_len]


# 示例
s = "33474"
print(longest_palindrome(s))  # 输出: 474
if __name__ == '__main__':
    pass
