'''
/*
Easy
1. BugfixingComputeMin
Find the bug(s) and modify one line of code in the incorrect implementation of a function solution that is supposed to return the smallest element
of the given non−empty array A which contains at most 1000 integers within range [-1000..1000].
Notice that fo  r the example test case A = [-1, 1, -2, 2] the attached code is already returning the correct answer (−2).
*/
'''

def test(arr) :
    ans = 0
    for i in range(1,len(arr)):
        if ans > arr[i]:
            ans = arr[i]
    return ans

'''
modify line 12 to ans[0]
'''
# class Test {
#     int test(int[] B, int[] C) {
#         int ans = 0;
#         for (int i = 1; i < B.length; i++) {
#             if (ans > B[I]) {
#                 ans = B[i];
#             }
#         }
#         return ans;
#     }
# }
