#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2024/3/12 下午12:10
# @Author: houhaiyang
# @Project: LeetCode-Python
# @File：数组移除相应元素后的长度.py
# @Description:考察双指针
# @company：
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = 0
        b = 0
        while a < len(nums):
            if nums[a] != val:
                nums[b] = nums[a]
                b += 1
            a += 1
        return b


if __name__ == '__main__':
    nums = [1, 2, 5, 2, 3]
    S = Solution()
    ret = S.removeElement(nums, 2)
    print(ret)
    pass
