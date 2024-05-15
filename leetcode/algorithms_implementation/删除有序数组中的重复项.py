#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2024/3/12 下午3:56
# @Author: houhaiyang
# @Project: LeetCode-Python
# @File：删除有序数组中的重复项.py
# @Description: 给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，
#               返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。
# @company：
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        slow = fast = 1
        while fast < n:
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


if __name__ == '__main__':
    # nums = [1]
    nums = [1, 1, 2, 2, 3, 3]
    S = Solution()
    ret = S.removeDuplicates(nums)
    print(ret)
    pass
