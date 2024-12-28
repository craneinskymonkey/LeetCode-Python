#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   build_tree.py
@Time    :   2024/07/04 00:11:00
@Author  :   haiyang.hou 
@Email   :   houhaiyang1991@gmail.com
@description   :   实现构建二叉树的功能
'''
class TreeNode(object):
    """
    二叉树数据类型
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(input_tree):
    '''
    构建二叉树
    '''
    if not input_tree:
        return None
    root = TreeNode(input_tree[0])
    queue = [root]  # 使用队列来进行层序遍历的构建
    index = 1  # 从数组的第二个元素开始（索引为1）
    while index < len(input_tree):
        node = queue.pop(0)  # 取出队列中的第一个节点
        if input_tree[index] is not None:  # 如果当前值不是None，则构建左子节点
            node.left = TreeNode(input_tree[index])
            queue.append(node.left)  # 将左子节点加入队列
        index += 1  # 移动到下一个值
        if index < len(input_tree) and input_tree[index] is not None:  # 如果当前值不是None，则构建右子节点
            node.right = TreeNode(input_tree[index])
            queue.append(node.right)  # 将右子节点加入队列
        index += 1  # 移动到下一个值
    return root  # 返回根节点