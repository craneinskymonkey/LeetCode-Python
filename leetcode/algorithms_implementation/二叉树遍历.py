#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2024/3/19 下午12:20
# @Author: houhaiyang
# @Project: LeetCode-Python
# @File：二叉树遍历.py
# @Description: 先序遍历二叉树
# @company：爱芯智元面试题


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root):
    result = []
    
    def traverse(node):
        if not node:
            return
        result.append(node.val)  # 访问根节点
        traverse(node.left)      # 递归遍历左子树
        traverse(node.right)     # 递归遍历右子树
    
    traverse(root)
    return result


if __name__ == '__main__':
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    ret = preorderTraversal(root)
    print(ret)



