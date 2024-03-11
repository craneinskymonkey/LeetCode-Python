#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2024/3/6 下午1:46
# @Author: houhaiyang
# @Project: LeetCode-Python
# @File：合并两个有序链表.py
# @Description: 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#               示例 ：输入：l1 = [1,2,4], l2 = [1,3,4]
#                     输出：[1,1,2,3,4,4]
# @company：国汽智控

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2

class Solution2:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        prehead = ListNode(-1)

        prev = prehead
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = list1 if list1 is not None else list2

        return prehead.next


if __name__ == '__main__':
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]

    # 创建有序链表对象
    l1 = ListNode(list1[0])
    l1.next = ListNode(list1[1])
    l1.next.next = ListNode(list1[2])

    l2 = ListNode(list2[0])
    l2.next = ListNode(list2[1])
    l2.next.next = ListNode(list2[2])

    S = Solution()
    ret = S.mergeTwoLists(l1, l2)
    print_list(ret)
