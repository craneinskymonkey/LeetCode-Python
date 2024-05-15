#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2024/2/24 下午2:40
# @Author: houhaiyang
# @Project: LeetCode-Python
# @File：最长递增子序列Leecode-300.py
# @Description:
# @company：
from typing import List

class longest_arithmetic_subsequence:

    """
    理想汽车面试题目
    给定一个整数序列，找到最长上升子序列（LIS），返回LIS的长度。考点：动态规划
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    def longestIncreasingSubsequence(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

if __name__ == '__main__':
    s = longest_arithmetic_subsequence()
    print(s.longestIncreasingSubsequence([10, 9, 2, 5, 3, 7, 4, 5]))
    pass