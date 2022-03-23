M= 1
N = 1
def zeroMatrix(mat):
    if M > 0 or N > 0:
        columnHash = {}#two hash table to mark the zeros
        rowHash = {}
        for i in range(M):
            for j in range(N):
                if mat[i][j] == 0:
                    if i not in columnHash:
                        columnHash[i] = 1
                    if j not in rowHash:
                        rowHash[j] = 1
        for i in columnHash:
            for j in range(N):
                mat[i][j] = 0
        for i in rowHash:
            for j in range(M):
                mat[j][i] = 0
    return
'''
Runtime: O(M x N)
Space: O(M x N)
'''


def displayMatrix( mat ):

    for i in range(0, M):

        for j in range(0, N):

            print (mat[i][j], end = ' ')
        print ("")



'''
test cases
regular - test with zeros on same rows and different matrix sizes
'''
# matrix = [[2],
#           [3],
#           [6],
#           [1]]

# matrix = [[1,2,3,4],
#         [5,1,0,8],
#         [9,2,1,0]]


# matrix = [[1,2,3,4],
#         [5,0,0,8],
#         [9,0,0,12],
#         [13,14,15,16]]

'''
extreme - size 1x1, empty matrix

'''

#matrix = []

#matrix = [[3]]


zeroMatrix(matrix)
displayMatrix(matrix)
