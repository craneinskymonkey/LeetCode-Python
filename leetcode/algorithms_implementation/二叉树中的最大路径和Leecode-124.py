#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2024/2/23 下午8:11
# @Author: houhaiyang
# @Project: LeetCode-Python
# @File：二叉树中的最大路径和Leecode-124.py
# @Description: 二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
#               路径和 是路径中各节点值的总和。
#               给你一个二叉树的根节点 root ，返回其 最大路径和。
# @company: 杭州罗博网络


class TreeNode(object):
    """
    二叉树数据类型
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 定义解决方案
    def __init__(self):
        self.maxSum = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        def maxGain(node):
            if not node:
                return 0

            # 递归计算左右子节点的最大贡献值
            # 只有在最大贡献值大于 0 时，才会选取对应子节点
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)

            # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
            priceNewpath = node.val + leftGain + rightGain

            # 更新答案
            self.maxSum = max(self.maxSum, priceNewpath)

            # 返回节点的最大贡献值
            return node.val + max(leftGain, rightGain)

        maxGain(root)
        return self.maxSum


def build_tree(input_tree):
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

def preorder_traversal(node):
    # 执行前序遍历（根左右）并打印节点值
    if node is not None:
        print(node.val, end=' ')
        preorder_traversal(node.left)
        preorder_traversal(node.right)
    print('---')  # 添加分隔符以帮助调试


if __name__ == '__main__':


    # 构建二叉树
    # root = TreeNode(-10)
    # root.left = TreeNode(9)
    # root.right = TreeNode(20)
    # root.right.left = TreeNode(15)
    # root.right.right = TreeNode(7)
    # preorder_traversal(root)



    input_tree = [-10, 9, 20, None, None, 15, 7]
    root = build_tree(input_tree)
    

    S = Solution()
    sum = S.maxPathSum(root)
    print('\n最大链路为:{}'.format(sum))