#include <iostream>
using namespace std;

void makeheap(int arr[], int n, int i)
{
    int root = i;
    int l = 2*i + 1;//left child index
    int r = 2*i + 2;//right child index

    if (l < n && arr[l] > arr[root]) //if the left child is larger
        root = l;

    if (r < n && arr[r] > arr[root]) //if the right child is larger
        root = r;

    if (root != i) //if any of the above situations
    {
        swap(arr[i], arr[root]); //swap them
        makeheap(arr, n, root); //repeat with the child
    }
}

void heapSort(int arr[], int n) //Ω(n log(n)) Θ(n log(n)) O(n log(n)) time complexity
//O(1) space complexity
{
    //make a heap
    for (int i = n / 2 - 1; i >= 0; i--)
        makeheap(arr, n, i); //goes through every node to make max heap
    for (int i=n-1; i>=0; i--) //each iteration eliminates one node
    {
        swap(arr[0], arr[i]); //swap root and the last
        makeheap(arr, i, 0); //autos starts at 0?
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
    heapSort(arr, size);
    for (int i=0; i < size; i++)
        std::cout << arr[i] << ";";
}
