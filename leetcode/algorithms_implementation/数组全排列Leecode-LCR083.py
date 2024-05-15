#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2024/2/24 下午1:58
# @Author: houhaiyang
# @Project: LeetCode-Python
# @File：数组全排列Leecode-LCR083.py
# @Description: 给定一个不含重复数字的整数数组 nums ，返回其 所有可能的全排列 。可以 按任意顺序 返回答案。 考点：回溯法
# company :  鉴智机器人

class Solution:

    def permute(self, nums):
        """
        :describe: 给定一个不含重复数字的数组 nums ，返回其所有可能的全排列 。你可以 按任意顺序 返回答案。
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res


if __name__ == '__main__':

    nums = [1, 2, 3]
    obj = Solution()
    ret = obj.permute(nums=nums)
    print(ret)
