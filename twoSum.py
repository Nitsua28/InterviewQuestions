"""
TWO SUM PROBLEM

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

1. may not use same element twice
2.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

"""


#O:N^2 runtime

def twoSum(nums, target):
	for i in range(len(nums)):
    		for j in range(len(nums)):
        		if i != j:
                sum = nums[i] + nums[j]
                if sum == target:
                	return [i, j]
    	return 0

#O:N run time
# def twoSum(nums, target):
# 	hashMap= {}
#     # Iterate through every element in numbers
#     for (i, element) in numbers.enumerated() {
#
#         #
#         Check if the hashMap contains an element
#         that with the current element, sums up to k.
#
#         if let mapped = hashMap[target - element] {
#            return [i, mapped]
#         }
#
#         # Add the element to the dictionary
#         hashMap[element] = i
#     }
#
#     /**
#     Return an empty array if unable to
#     find a pair that adds up to the target.
#     */
#     return []
def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap= {}
    # Iterate through every element in numbers
        for i in range(len(nums)):

            if target - nums[i] in hashMap:
                return [hashMap[target - nums[i]], i]

        # Add the element to the dictionary
            hashMap[nums[i]] = i

        return []
# for every element in num, if target - elemnt exists in hash map
 # then return the indices otherwise add it to hash map.
"""
twoSum([2,7,11,15], 9)
target=9
hash={2:0, }
i=1
nums[i]=7
target-nums[i]=2

found return = [2,1]

"""
"""
twoSum([3,2,4], 6)
target= 6
hash={3:0,2:1,}
i=2
nums[i]=4
target-nums[i]=2

found return=[1,2]
"""
"""
twoSum([1,2,3], 3)
"""
length = 3

i = 0
j = 0
skip

i = 0
j = 1
no break
nums[i] = 1
nums[j] = 2
sum = 3
if pass
return [0,1]


"""
twoSum([1,0,2],2)
[0,0]
"""
