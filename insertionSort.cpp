#include <iostream>
using namespace std;
void insertionSort(int *array, int size) {//  Ω(n) Θ(n^2) O(n^2) time complexity
  //  O(1) space complexity
  
   int key, j, k;
   //i starts at 1 due to the fact that the first element is labeled as sorted first.
   for(int i = 1; i<size; i++) {
      key = array[i];//take value to be focused on
      j = i;//take location of key and set it to j and k
      k = j;
      //checks each element of sorted region backwards and stops if element before is less than key
      while(j > 0 && array[j-1]>key) {
        array[j] = array[j-1]; //if element before is less than key then it becomes the element
        j--;
      }
      array[j] = key;   //insert in right place if exited while loop
      int count = 0;// counts up to k to output snapshot

      //for sake of this assignment it outputs snapshot of whenever key is inserted
      // while (count <= k)
      // {
      //   cout << array[count] << ";";
      //   count++;
      // }
      // cout << endl;
   }
}
int main()
{
    int *arr; //pointer array to be changed while in scope of function
    int size;
    cin >> size;
    arr = new int[size];
    for (int i = 0; i < size; i++)
        cin >> arr[i];
    insertionSort(arr, size);
    return 0;
}
