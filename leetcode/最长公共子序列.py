#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2024/3/7 上午11:32
# @Author: houhaiyang
# @Project: LeetCode-Python
# @File：最长公共子序列.py
# @Description:
# @company：

class solution():
    def longestsubcommonsuquence(self, str1, str2):
        m = len(str1)
        n = len(str2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
if __name__ == '__main__':
    str1 = 'abcde'
    str2 = 'ace'
    S = solution()
    ret = S.longestsubcommonsuquence(str1, str2)
    print(ret)




