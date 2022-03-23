#runtime of log of n
#with each iteration the size of n is n/2 of previous
def search(self, nums: List[int], target: int) -> int:
        r = len(nums) - 1 #low as 0 and high as size-1 because the indices need to be input.
        l = 0
        while r >= l:#high >= low to eliminate the case
    #where the array gets to be the smallest aka high = low

            mid = l + ((r - l) // 2)#given the array is already sorted
    # //we choose the mid as a marker to see if
    # //search is lower or higher than it

            # If element is present at the middle itself
            if nums[mid] == target:
                return mid

            # If element is smaller than mid, then it
            # can only be present in left subarray
            elif nums[mid] > target:
                r = mid - 1

            # Else the element can only be present
            # in right subarray
            else:
                l = mid + 1

            # Element is not present in the array
        return -1
