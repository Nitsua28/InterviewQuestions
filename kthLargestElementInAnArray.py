'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.
'''
'''
example
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
constraints

    1 <= k <= nums.length <= 104
    -104 <= nums[i] <= 104

'''
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)

    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
        for i in range(n // 2 - 1, -1, -1):
            heapify(nums, n, i)

        # One by one extract elements
        for i in range(n-1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]   # swap
            heapify(nums, i, 0)
        return nums[-abs(k)]
