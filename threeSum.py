#O(n^3) runtime
def find3Numbers(A, arr_size, sum):

    # Fix the first element as A[i]
    for i in range( 0, arr_size):

        # Fix the second element as A[j]
        for j in range(i + 1, arr_size):

            # Now look for the third number
            for k in range(j + 1, arr_size):
                if A[i] + A[j] + A[k] == sum:
                    print("Triplet is", A[i],
                          ", ", A[j], ", ", A[k])
                    return True

    # If we reach here, then no
    # triplet was found
    return False

def find3Numbers(A, arr_size, sum):
    ans = []
    for i in range(0, arr_size-1):
        # Find pair in subarray A[i + 1..n-1]
        # with sum equal to sum - A[i]
        s = set()
        curr_sum = sum - A[i]
        for j in range(i + 1, arr_size):
            if (curr_sum - A[j]) in s:
                ans.append([A[i],A[j]],curr_sum-A[j])
            s.add(A[j])

    return ans
"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:

Input: nums = []
Output: []

Example 3:

Input: nums = [0]
Output: []



Constraints:

    0 <= nums.length <= 3000
    -105 <= nums[i] <= 105

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #nums.sort()
        #ans = []
        #for i in range(0, len(nums)-1):
        #    if i != 0 and nums[i] == nums[i+1]:
        #        continue
        #    s = set()
        #    for j in range(i + 1, len(nums)):

        #        if ((0-nums[i]) - nums[j]) in s:
        #            ans.append([nums[i], nums[j], (0-nums[i]) - nums[j]])
        #        while nums[j]==nums[j+1] and (j+1) <= len(nums):
        #            j+=1
        #        s.add(nums[j])
        #return ans

        result = []
        nums.sort() #sort for id duplicates
        for idx, num in enumerate(nums):
            target = -num# target is 0
            if idx > 0 and num == nums[idx-1]:
                continue
            hm = {}
            for i, n in enumerate(nums[idx+1:]):
                if target-n in hm:
                    if i+idx+2 < len(nums) and n == nums[i+idx+2]:
                        continue
                    triplets = [num, target-n, n]
                    result.append(triplets)
                else:
                    hm[n] = 1
        return result
