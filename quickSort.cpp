#include <iostream>
#include <cstdlib>
#include <time.h>
using namespace std;
int partition (int arr[], int low, int high)
{
    int pivot = arr[high]; //pivot is set at the highest index
    int i = low - 1;  //i calculates the counter where the pivot is switched to the correct position

    for (int j = low; j <= high- 1; j++)//j increments through all the array to see if less than pivot
    {
        // If current element is smaller than the pivot
        if (arr[j] < pivot)
        {
            i++;    // increment counter
            swap(arr[i], arr[j]);//shove less than elements to left
        }
    }
    swap(arr[i + 1], arr[high]);//put pivot to correct position
    return i + 1;//return position of pivot

}
int partition_rand(int arr[], int low, int high)
{
    srand(time(NULL)); //initializes random number generator
    int random = low + rand() % (high - low); //chooses a random index
    swap(arr[random], arr[high]); //switches that value to the highest index
    return partition(arr, low, high); //does regular quicksort
}

void quickSort(int arr[], int low, int high)//Ω(n log(n)) Θ(n log(n)) O(n^2) time complexity
//O(log(n)) space complexity
{
    if (low < high)  //for base case size 1
    {

        int pivot = partition_rand(arr, low, high);
        quickSort(arr, low, pivot - 1);  //repeats with the left and right side of the pivot
        quickSort(arr, pivot + 1, high);
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
    quickSort(arr, 0, size - 1);
    /* print out array in correct format*/
    for (int i=0; i < size; i++)
        std::cout << arr[i] << ";";
    return 0;
}
