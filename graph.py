"""
given a 2d matrix
"""

matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
]

class Node:
    def __init__(self,val,coor):
        self.val = val
        self.coor = coor
#make children nodes when making nodes recursively?
class Graph:
    def __init__(self,mat = None):
        self.mat = mat
        self.sizey = len(mat)
        self.sizex = len(mat[0])
        self.childList = {}

        if self.sizey < 1 and self.sizex < 1:
            return


        for i in range(self.sizey):

            for j in range(self.sizex):

                temp = []

                if self.sizey != 1:
                    if i != 0 and i != self.sizey-1:
                        temp.append(Node(self.mat[i+1][j],(str(i+1)+","+str(j))))
                        temp.append(Node(self.mat[i-1][j],(str(i-1)+","+str(j))))
                    elif i == 0:
                        temp.append(Node(self.mat[i+1][j],(str(i+1)+","+str(j))))
                    else:
                        temp.append(Node(self.mat[i-1][j],(str(i-1)+","+str(j))))
                if self.sizex != 1:
                    if j != 0 and j != self.sizex-1:
                        temp.append(Node(self.mat[i][j+1],(str(i)+","+str(j+1))))
                        temp.append(Node(self.mat[i][j-1],(str(i)+","+str(j-1))))
                    elif j == 0:
                        temp.append(Node(self.mat[i][j+1],(str(i)+","+str(j+1))))
                    else:
                        temp.append(Node(self.mat[i][j-1],(str(i)+","+str(j-1))))
                tempStr = str(i) + "," + str(j)
                self.childList[tempStr]=temp

myGraph = Graph(matrix)
