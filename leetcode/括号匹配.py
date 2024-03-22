#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2024/3/19 下午12:28
# @Author: houhaiyang
# @Project: LeetCode-Python
# @File：括号匹配.py
# @Description:
                # 面试题08.09. 括号
                # 括号。设计一种算法，打印n对括号的所有合法的（例如，开闭一一对应）组合。
                # 说明：解集不能包含重复的子集。
                # 例如，给出 n = 3，生成结果为：
                # [
                #  "((()))",
                #  "(()())",
                #  "(())()",
                #  "()(())",
                #  "()()()"
                #]

# @company： 爱芯元智

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()

        backtrack([], 0, 0)
        return ans

if __name__ == '__main__':
    # 回塑法
    A = Solution()
    ret = A.generateParenthesis(3)
    print(ret)


