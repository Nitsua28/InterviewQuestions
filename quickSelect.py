arr = [9,8,7,6,5,4,3,2,1]
def findKth(nums,k):
    quickSelect(nums, 0, len(nums)-1,k)
    k = len(nums) - k
    return nums[k]
def quickSelect(A, low, high, k):
    if low < high:
        parti = lomutoPartition(A, low, high)
        index = len(A) - k
        if parti == index:
            return
        elif parti < index:
            quickSelect(A, parti+1, high, k)
        else:
            quickSelect(A, low, parti-1, k)

def lomutoPartition(A, low, high):
    pivot = A[high]
    i = low-1
    for j in range(low, high): #not including pivot!
        if pivot >= A[j]:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[high] = A[high], A[i+1]
    return i+1

print(findKth(arr,2))

print(arr)


'''
[1,3,2,4]

piv

parti = 0
index = 2

k = 2
low = 0
high = 3
'''
