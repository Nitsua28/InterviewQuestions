
#include<iostream>
#include<stdio.h>
#include<limits.h>
int numRodsUsed; //keeps track of # of rods used

int cutRod(int price[], int rods[], int s)
{
  int val[s+1];
  int lastRodCut[s+1];
  val[0] = 0;
  int i, j;
//bottom up implementation
  for (i = 1; i<=s; i++)
  {
      int max_val = INT_MIN;
      int rodlen = -1;
      for (j = 0; j < i; j++)
        {
           if (max_val < price[j] + val[i-j-1])
           {
               max_val = price[j] + val[i-j-1];
               rodlen = j;
           }
        }
      val[i] = max_val;
      lastRodCut[i] = rodlen + 1;
  }

  for (i = s, j = 0; i > 0; i -= lastRodCut[i])
  {
      rods[j++] = lastRodCut[i];
  }
  numRodsUsed = j;

  return val[s];
}

int main()
{
   int s;
   std::cin >> s;
   int arr[s], rodsused[s+1], i;
   for (i = 0; i < s; i++)
       std::cin >> arr[i];

   int max = cutRod(arr, rodsused, s);
   std::cout << max << "\n";

   for (i = 0; i < numRodsUsed; i++)
       std::cout << rodsused[i] << " ";
   std::cout << "-1\n";

   return 0;
}
