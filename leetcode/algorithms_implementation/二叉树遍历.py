#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2024/3/19 下午12:20
# @Author: houhaiyang
# @Project: LeetCode-Python
# @File：二叉树遍历.py
# @Description:
# @company：爱芯智元面试题


def inorder_traversal(node):
    # 执行前序遍历（根左右）并打印节点值
    if node is not None:
        print(node.val, end=' ')
        inorder_traversal(node.left)
        inorder_traversal(node.right)

def build_tree(input_tree):
    return root

if __name__ == '__main__':
    input_tree = [-10, 9, 20, None, None, 15, 7]
    root = build_tree(input_tree)
    inorder_traversal(root)



