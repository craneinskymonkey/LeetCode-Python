import collections
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = collections.Counter(nums1)
        counter2 = collections.Counter(nums2)
        result = []

        for key, value in counter1.items():
            if key in counter2:
                result.extend([key] * min(value, counter2[key]))

        return result
