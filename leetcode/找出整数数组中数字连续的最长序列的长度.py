#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2024/3/7 下午7:01
# @Author: houhaiyang
# @Project: LeetCode-Python
# @File：找出整数数组中数字连续的最长序列的长度.py
# @Description: 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
# @company： smart汽车
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)

        return longest_streak


if __name__ == '__main__':
    nums = [0, 3, 7, 2, 5, 8,  6, 0, 1]
    S = Solution()
    print(S.longestConsecutive(nums))
