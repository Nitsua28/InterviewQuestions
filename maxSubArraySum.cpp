#include <stdio.h>
#include <limits.h>
#include <iostream>

//extra function to calculate max of two integers
int max(int a, int b)
{
    return (a > b)? a : b; // if true return a, if not return b
}
//extra function to calculate max of three integers
int max(int a, int b, int c)
{
    return max(max(a, b), c);
}
int maxCrossingSum(int arr[], int l, int m, int h)
{
    // add elements on left side
    int sum = 0;
    int left_sum = INT_MIN;
    for (int i = m; i >= l; i--)
    {
        sum = sum + arr[i];
        if (sum > left_sum)
          left_sum = sum;
    }
    // add elements on right side
    sum = 0;
    int right_sum = INT_MIN;
    for (int i = m+1; i <= h; i++)
    {
        sum = sum + arr[i];
        if (sum > right_sum)
          right_sum = sum;
    }
    // Return sum of left and right
    return left_sum + right_sum;
}

int maxSubArraySum(int arr[], int l, int h)
{
    // base case: Only one element
   if (l == h)
     return arr[l];
    // find midpoint
   int m = (l + h)/2;
  /* Return maximum of following three possible cases
      a) Maximum subarray sum in left half
      b) Maximum subarray sum in right half
      c) Maximum subarray sum such that the subarray crosses the midpoint */
   return max(maxSubArraySum(arr, l, m),
              maxSubArraySum(arr, m+1, h),
              maxCrossingSum(arr, l, m, h));
}
int main()
{
    int *arr;
    int size;
    std::cin >> size;
    arr = new int[size];
    for (int i = 0; i < size; i++)
        std::cin >> arr[i];
    int max_sum = maxSubArraySum(arr, 0, size-1);
    std::cout << max_sum;
    return 0;
}
