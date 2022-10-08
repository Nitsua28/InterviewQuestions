import unittest


class testRunningSum(unittest.TestCase):
    def test_regular(self):
        self.assertEqual(pivotIndex([1, 7, 3, 6, 5, 6]), 3)

    def test_edge(self):
        self.assertEqual(pivotIndex([0]), 0)

    def test_edge2(self):
        self.assertEqual(pivotIndex([1, 3, 4]), -1)

    def test_edge3(self):
        self.assertEqual(pivotIndex([1]), 0)

    def test_negative(self):
        self.assertEqual(pivotIndex([-2, -1, -7, -3]), 2)

# 1 <= nums.length <= 104
# -1000 <= nums[i] <= 1000

def pivotIndex(nums):
    answer = -1

    for i in range(len(nums)):

        j = i
        k = i
        suml = 0
        sumr = 0

        while j > 0:
            j-=1
            suml += nums[j]

        while k < len(nums) - 1:
            k+=1
            sumr += nums[k]

        if suml == sumr:
            answer = i
            break
            
    return answer

if __name__ == '__main__':
# Test Cases
    unittest.main()
