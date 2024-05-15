#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2024/3/6 下午8:18
# @Author: houhaiyang
# @Project: LeetCode-Python
# @File：判断两个二叉树是否相等.py
# @Description:
# @company：轻舟智航
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    # 如果两个节点都为空，则它们是相同的
    if p is None and q is None:
        return True
        # 如果一个节点为空，而另一个不为空，则它们不相同
    if p is None or q is None:
        return False
        # 如果节点的值不相同，则它们不相同
    if p.val != q.val:
        return False
        # 递归地检查左子树和右子树
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
