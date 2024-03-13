#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2024/3/12 下午12:20
# @Author: houhaiyang
# @Project: LeetCode-Python
# @File：合并两个有序数组.py
# @Description: 合并两个有序数组，先合并再排序思想
# @company：
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        nums1.sort()


if __name__ == '__main__':
    nums1 = [1, 2, 3, 4]
    nums2 = [2, 3, 4, 5]
    S = Solution()
    S.merge(nums1, 4, nums2, 4)
    pass
