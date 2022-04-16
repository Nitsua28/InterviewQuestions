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

'''
using quickselect

'''

def quickSelect(A, F,low, high, k):
    if low < high:
        parti = lomutoPartition(A,F, low, high)
        index = len(A) - k
        if parti == index:
            return
        elif parti < index:
            quickSelect(A, F, parti+1, high, k)
        else:
            quickSelect(A, F, low, parti-1, k)

def lomutoPartition(A, F,low, high):
    pivot = F[A[high]]
    i = low-1
    for j in range(low, high): #not including pivot!
        if pivot >= F[A[j]]:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[high] = A[high], A[i+1]
    return i+1
class Solution:


    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        numsUni = list(count.keys())
        quickSelect(numsUni,count,0,len(numsUni)-1,k)
        index = len(numsUni) - k
        return numsUni[index:]
