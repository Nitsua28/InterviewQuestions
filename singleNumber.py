"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,1]
Output: 1

Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

Example 3:

Input: nums = [1]
Output: 1



Constraints:

    1 <= nums.length <= 3 * 104
    -3 * 104 <= nums[i] <= 3 * 104
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #make hash map and for every i, put in key: 1 and if repeat just take off.
        #linear time
        #linear space
        hash = {}
        for i in nums:
            try:
                hash.pop(i)
            except:
                hash[i] = 1
        return hash.popitem()[0]
