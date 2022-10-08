import unittest


class testRunningSum(unittest.TestCase):
    def test_regular(self):
        self.assertEqual(runningSum([1, 2, 3]), [1, 3, 6])

    def test_edge(self):
        self.assertEqual(runningSum([0]), [0])

    def test_negative(self):
        self.assertEqual(runningSum([-2, -1, -7]), [-2, -3, -10])
# Given an array nums.
# We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

# Constraints:
#
# 1 <= nums.length <= 1000
# -10^6 <= nums[i] <= 10^6


def runningSum(nums):
    ''' returns the running sum of an array of numbers
        Example: [1, 2, 3] Running Sum: [1, 3, 6] '''

    runningSum = []
    sum = 0

    for i in nums:
        sum += i
        runningSum.append(sum)
    return runningSum

if __name__ == '__main__':
# Test Cases
    unittest.main()
# regular
