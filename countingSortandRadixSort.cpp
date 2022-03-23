#include<iostream>
using namespace std;
void countSort(int arr[][10], int size, int digit)//Ω(n+k) Θ(n+k) O(n+k) time complexity
//O(k) space complexity
{
    int output[size][10] = { 0 }; // output array
    int i,j, count[4] = { 0 };
    // Store count of occurrences in count[]
    for (i = 0; i < size; i++)
        count[arr[i][digit]]++;
    //numbers limited to 0-3
    for (i = 1; i < 4; i++)
        count[i] += count[i - 1];
    //for every sorted number sort the row
    for (i = size - 1; i >= 0; i--)
    {
        //std::cout << "h1";
        for (int j = 0; j < 10; j++)
        {
            output[count[ arr[i][digit] ]-1][j] = arr[i][j];
        }
        count[ arr[i][digit] ]--;
        //std::cout << "h2";
    }
    //replace the array
    for (i = 0 ; i < size ; i++)
        {
            for(j = 0; j < 10; j++)
                arr[i][j] = output[i][j];
        }
}

// The main function to that sorts arr[] of vectornum size using
// Radix Sort
void radixsort(int arr[][10], int size)//Ω(nk) Θ(nk) O(nk) timecomplexity
//O(n+k) space complexity
{
    //for every digit sort the row
    for (int i = 9; i >= 0; i--)
        {
            countSort(arr, size, i);
        }
}
int main()
{
    int i, j;
    int vectornum;
    std::cin >> vectornum;
    int arr [vectornum] [10];
    //input into 2d matrix
    for (i = 0; i < vectornum; i++)
        {
            std::cin >> arr[i][0] >> arr[i][1] >> arr[i][2] >> arr[i][3] >> arr[i][4]
            >> arr[i][5] >> arr[i][6] >> arr[i][7] >> arr[i][8] >> arr[i][9];
        }
   radixsort(arr, vectornum);
    for (i = 0; i < vectornum; i++)
        {
            for(j = 0; j < 10; j++)
                std::cout << arr[i][j] << ";";
            std::cout << "\n";
        }
    return 0;
}
