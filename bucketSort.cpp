#include <iostream>
#include <vector>
#include <algorithm>
void bucketSort(float *arr, int size)
{
    std::vector <float> temp[10]; //since floating point numbers < 1
    //we make a bucket array of 1-10 for numbers between 0-1

    //place in buckets
    for (int i = 0; i< size; i++)
    {
        int y = arr[i]* 10; //determine the  bucket to be placed in  based on value
        temp[y].push_back(arr[i]);
    }
    //sorts each bucket
    for (int i = 0; i< 10; i++)
    {
        float key;
        for(int j = 1; j<temp[i].size(); j++) //insertionsort
            {
                key = temp[i][j];
                int z = j;
                    while(z > 0 && temp[i][z-1]>key) {
                    temp[i][z] = temp[i][z-1];
                    z--;
                    }
                temp[i][z] = key;
            }
    }
    int count = 0;
    //concatenates all the sorted buckets
    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < temp[i].size(); j++)
        {
            arr[count] = temp[i][j];
            count++;
        }
    }
//Bucket sort Best case and avg: O(n+k) when uniformly distributed
//            Worst case: O(n^2)
//space complexity : O(n)

}
int main()
{
    float *arr;
    int size;
    std::cin >> size;
    arr = new float[size];
    for (int i = 0; i < size; i++)
        std::cin >> arr[i];
    bucketSort(arr,size);
    for (int i = 0; i < size; i++)
        std::cout << arr[i] << std::endl;
    return 0;
}
