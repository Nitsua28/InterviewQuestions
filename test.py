arr = [3,2,1,5,6,4]
def insertionSort(arr):
    for i in range(1, len(arr)):

        key = arr[i]
        j = i #counter for every key
        while j > 0 and arr[j-1] > key: #stops if key finds greater or runs out
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = key
    return arr

print(insertionSort(arr))
