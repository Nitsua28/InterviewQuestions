"""
Given an integer array nums sorted in non-decreasing order, return an array
of the squares of each number sorted in non-decreasing order.



Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]



Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in non-decreasing order.
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        squaredArr = [None] * n#as big as nums
        highestSquareIndex = n - 1

        left = 0
        right = n - 1

        while left <= right:
            leftSquare = nums[left] ** 2
            rightSquare = nums[right] ** 2
            #two pointers pointing to positive side and the negative side and square them and add to new subarray
            #O(n) time complexity
            #0(n) space complexity
            if leftSquare > rightSquare:
                squaredArr[highestSquareIndex] = leftSquare
                highestSquareIndex-=1
                left+=1
            else:
                squaredArr[highestSquareIndex] = rightSquare
                highestSquareIndex-=1
                right-=1
        return squaredArr

"""
input [-4,-1,0,3,10]
aqrarr= [0,1,9,16,100]
highestSquareIndex=-1
left = 2
right = 1
leftsquare =0
rightsquare =0
n = 5
"""

"""
input [-7,-6,1,4,7,9]
aqarr= [1,16,36,49,49,81]
highestSquareIndex=0
left=2
right=1
leftsquare=1
rightsquare=1
n=6
"""
