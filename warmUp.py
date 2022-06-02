def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap= {}
    # Iterate through every element in numbers
        for i in range(len(nums)):

            if target - nums[i] in hashMap:
                return [hashMap[target - nums[i]], i]

        # Add the element to the dictionary
            hashMap[nums[i]] = i

        return []
