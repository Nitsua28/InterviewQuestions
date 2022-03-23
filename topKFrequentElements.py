'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

constraints:

    1 <= nums.length <= 105
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.

    Example 1:

    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [i for i, j in Counter(nums).most_common(k)]
