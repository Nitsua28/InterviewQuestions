arr = [1,2,5,6,7]
def insertionSort(arr):
    for i in range(1, len(arr)):

        key = arr[i]
        j = i #counter for every key
        while j > 0 and arr[j-1] > key: #stops if key finds greater or runs out
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = key
    return arr
# insertion sort O(n^2) best case is when already sorted and small n. cheap efficent
#inplace?
#stable

def insertionSort(arr):
    for i in range(1,len(arr)):

[2,3,5,5,6,7]
i=5
j=3
arr[j-1] = 7
key =6

def mergeSort(arr):
    if len(arr) > 1:
        a = len(arr)//2 #
        l = arr[:a]
        r = arr[a:]

        # Sort the two halves
        #stable
        #nlogn run time
        mergeSort(l)
        mergeSort(r)

        b = 0
        c = 0
        d = 0

        while b < len(l) and c < len(r): #actual sorting goes through and compares elements in two arrays

            if l[b] < r[c]:
                arr[d] = l[b]
                b += 1
            else:
                arr[d] = r[c]
                c += 1
            d += 1

        while b < len(l):
            arr[d] = l[b]
            b += 1
            d += 1

        while c < len(r):
            arr[d] = r[c]
            c += 1
            d += 1
def quicksort(A, low, high):
    if low < high:
        parti = lomutoPartition(A, low, high)
        quicksort(A, low, parti-1)
        quicksort(A, parti+1, high)

def lomutoPartition(A, low, high):
    pivot = A[high]
    i = low-1
    for j in range(low, high): #not including pivot!
        if pivot >= A[j]:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[high] = A[high], A[i+1]
    return i+1
'''
quicksort is not stable
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

# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)
'''
not stable: operations change the order
inplace
nlogn runtime
'''
def printArr(arr):
    print(arr)
print(arr)
print(quicksort(arr,0,4))
print(arr)
