N = 4

def rotateMatrix(mat):
#counterclockwise
def rotateMatrixInPlace(mat):
#depending on the value of N, both iterations is affected
# time complexity O(N*N) one traversal of entire matrix
# space complexity O(1) inplace
    for x in range(0, int(N / 2)):

        for y in range(x, N-x-1):#for every iteration, 4 elements are shifted

            temp = mat[x][y] #store in temp because mat[x][y] knowledge is erased
            #-1 for the indices
            mat[x][y] = mat[y][N-1-x] #top is replaced

            mat[y][N-1-x] = mat[N-1-x][N-1-y]#right column replaced

            mat[N-1-x][N-1-y] = mat[N-1-y][x]#bottom replaced

            mat[N-1-y][x] = temp #left replaced


def displayMatrix( mat ):

    for i in range(0, N):

        for j in range(0, N):

            print (mat[i][j], end = ' ')
        print ("")




# Driver Code
mat = [[0 for x in range(N)] for y in range(N)]

# Test case 1
mat = [ [1, 2, 3, 4 ],
        [5, 6, 7, 8 ],
        [9, 10, 11, 12 ],
        [13, 14, 15, 16 ] ]
'''
#test matrix
#temp = 6
[4, 8, 12, 16]
[3, 7, 11, 15]
[2, 6, 10, 14]
[1, 5, 9, 13]

#x = 1 #N/2 = 2
#y = 2 #N-x-1 = 3
#N = 4
#N-1-x =
#N-1-y =
'''

'''
# Test case 2
temp = 2
mat = [ [3, 6, 9 ],
        [2, 5, 8 ],
        [1, 4, 7 ] ]

#x = 0 #N/2 = 1
#y = 0 #N-x-1 = 2
#N = 3
#N-1-x =2
#N-1-y =2

# Test case 3
temp = 1
mat = [ [2, 5 ],
        [1, 4 ] ]

#x = 0 #N/2 = 1
#y = 0 #N-x-1 = 1
#N = 2
#N-1-x =2
#N-1-y =2
'''

rotateMatrixInPlace(mat)

# Print rotated matrix
displayMatrix(mat)
