#include <iostream>
void merge(int arr[], int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1; //left half size
    int n2 =  r - m; //right half size

    int L[n1], R[n2]; //temp array of sizes of halfs

    /* copies the halfs to these temps */

    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    i = 0;
    j = 0;
    k = l;

    /* i controls indices of left half
        j controls indices of right half
        k controls where the merge copies on the actual array */

    //actual sorting
    while (i < n1 && j < n2) //iterates trhough the temp array until max size
    {
        //compares each indices to see if greater and then adds the lesser to the actual array
        if (L[i] <= R[j])
        {
            arr[k] = L[i]; //adds lesser then increments
            i++;
        }
        else
        {
            arr[k] = R[j]; //adds lesser then increments
            j++;
        }
        k++; //increments place in actual array
    }
    while (i < n1) //eventually comparasion stops and there might be numbers left starting from left side
    {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2)
    {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void mergeSort(int arr[], int l, int r) //Ω(n log(n)) Θ(n log(n)) O(n log(n)) time complexity
//O(n) space complexity
{
    if (l < r) // goes in only if l -= r eliminating possibility of empty array?
    {
        int m = (l+r)/2; //finds midpoint index
        mergeSort(arr, l, m); //splits left half recursively
        mergeSort(arr, m+1, r); //splits right half recursively
        merge(arr, l, m, r); //combines and sorts together
    }
}
int main()
{
    int *arr;
    int size;
    std::cin >> size;
    arr = new int[size];
    for (int i = 0; i < size; i++)
        std::cin >> arr[i];
    mergeSort(arr,0, size-1);//size -1 for the array indices for parameters

    /* print out array in correct format*/
    for (int i=0; i < size; i++)
        std::cout << arr[i] << ";";
    return 0;
}
