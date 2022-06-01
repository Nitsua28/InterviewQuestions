arr = [4,7,3,2,1]

def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i
        while j > 0 and arr[j - 1] > key:
            arr[j] = arr[j-1]
            j-=1
        arr[j] = key
    return arr

[1,2,3,4,7]

key = 7

def mergeSort(arr):
    if len(arr) > 1:
        m = len(arr) // 2
        left = arr[:m]
        right = arr[m:]

        mergeSort(left)
        mergeSort(right)

        l = r = a = 0

        while l < len(left) and r < len(right):

            if left[l] < right[r]:
                arr[a] = left[l]
                l+=1
            else:
                arr[a] = right[r]
                r+=1
            a+=1

        while l < len(left):
            arr[a] = left[l]
            l+=1
            a+=1

        while r < len(right):
            arr[a] = right[r]
            r+=1
            a+=1

[4,7,3,2,1]

[4,7] [3,2,1]
[4] [7] [3] [2,1]
[4] [7] [3] [2] [1]
[4] [7] [3] [1,2]
[4,7] [1.2.3]
[1,2,3,4,7]
def lmutopartition(arr,low,high):
    pivot = arr[high]
    j = low -1
    for i in range(low, high):
        if pivot >= arr[i]:
            arr[i], arr[j] = arr[j], arr[i]
            j-=1
    arr[high], arr[j+1] = arr[j+1], arr[high]
    return j+1
def quicksort(arr, low, high):
    if low < high:
        part = lumotopartition(arr, low, high)
