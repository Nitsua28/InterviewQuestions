"""
given a 2d matrix

Island
2D-Grid of Integers
Height Map

Rain Fall -- Flows from high to low. Ties don’t count, needs to be strictly smaller.
Given a spot on island, return whether or not the rain will reach any edges of the island.
Water can only traverse in 4 cardinal directions

contraints

2d matrix nxm

0<n< inf
0<m<inf

0<element<inf
"""

# islandMatrix= [
#         [9,9,9,4,9],
#         [9,1,3,1,9],
#         [9,1,9,1,9],
#         [9,1,3,2,9],
#         [9,9,9,1,9]
# ]
#works
# islandMatrix= [[9,9,9],
#                [9,8,9],
#                [9,9,9]]
#works
islandMatrix=[[1,1,9,1,1],
              [1,7,8,7,1],
              [9,8,9,8,9],
              [1,7,8,7,1],
              [1,1,9,1,1]]

class Graph:
    def __init__(self,matrix = None):
        self.matrix = matrix
        self.sizey = len(matrix)

        if self.sizey == 0:#segmentation fault bypass
            self.sizex = 0
        else:
            self.sizex = len(matrix[0])

        self.parentValMatrix = [[None for i in range(self.sizex)] for j in range(self.sizey)]

    def isAllEdge(self):
        return self.sizex < 3 or self.sizey < 3

    def matrixIsEmpty(self):
        return self.sizey == 0

    def isOutOfRange(self,x,y):
        return 0 > x or x > self.sizex or 0 > y or y > self.sizey

    def isOnEdge(self,x,y):
        return x == 0 or y == 0 or x == self.sizex-1 or y == self.sizey-1 or self.isAllEdge()

    def isLessThanParent(self,x,y):
        temp = self.parentValMatrix[y][x].split(",")
        xCoordinate = int(temp[0])
        yCoordinate = int(temp[1])
        return self.matrix[y][x] < self.matrix[yCoordinate][xCoordinate]
    def isEmpty(self,x,y):
        return self.parentValMatrix[y][x] is None
    def pushChild(self,list, child, isStack=False):
        if isStack:
            list.append(child)
        else:
            list.insert(0,child)

    def populate(self,x,y, list, isStack=False, isRoot=False):
        if y != 0 and y != self.sizey-1:
            if self.isEmpty(x,y+1) or isRoot:
                self.parentValMatrix[y+1][x] = str(x) + "," + str(y)
                self.pushChild(list, str(x) + "," + str(y+1), isStack)
            if self.isEmpty(x,y-1) or isRoot:
                self.parentValMatrix[y-1][x] = str(x) + "," + str(y)
                self.pushChild(list, str(x) + "," + str(y-1), isStack)
        elif y == 0:
            if self.isEmpty(x,y+1) or isRoot:
                self.parentValMatrix[y+1][x] = str(x) + "," + str(y)
                self.pushChild(list, str(x) + "," + str(y+1), isStack)
        else:
            if self.isEmpty(x,y-1) or isRoot:
                self.parentValMatrix[y-1][x] = str(x) + "," + str(y)
                self.pushChild(list, str(x) + "," + str(y-1), isStack)

        if x != 0 and x != self.sizex-1:
            if self.isEmpty(x+1,y) or isRoot:
                self.parentValMatrix[y][x+1] = str(x) + "," + str(y)
                self.pushChild(list, str(x+1) + "," + str(y), isStack)
            if self.isEmpty(x-1,y) or isRoot:
                self.parentValMatrix[y][x-1] = str(x) + "," + str(y)
                self.pushChild(list, str(x-1) + "," + str(y), isStack)
        elif x == 0:
            if self.isEmpty(x+1,y) or isRoot:
                self.parentValMatrix[y][x+1] = str(x) + "," + str(y)
                self.pushChild(list, str(x+1) + "," + str(y), isStack)
        else:
            if self.isEmpty(x-1,y) or isRoot:
                self.parentValMatrix[y][x-1] = str(x) + "," + str(y)
                self.pushChild(list, str(x-1) + "," + str(y), isStack)
    def printPath(self,rootx,rooty,edgex,edgey):
        root = str(rootx) + "," + str(rooty)
        x = edgex
        y = edgey
        print("edge: "+ str(x) + "," + str(y))
        count = 0
        while self.parentValMatrix[y][x] != root and count < 10:
            print(self.parentValMatrix[y][x])
            tempCoor = self.parentValMatrix[y][x].split(",")
            x = int(tempCoor[0])
            y = int(tempCoor[1])
            count += 1
        print("root=" + root)
    def printParentValMatrix(self):
        for i in self.parentValMatrix:
            for j in i:
                print( j, end="")
                print(" ", end="")

            print()


myGraph = Graph(islandMatrix)

def dfs(graph,x,y): #depth first search
    if graph.matrixIsEmpty():
        print("graph is empty")
        return
    if graph.isOutOfRange(x,y):
        print("invalid spot")
        return
    if graph.isOnEdge(x,y):
        return True

    spotNode = str(x) + "," + str(y)
    graph.parentValMatrix[y][x] = spotNode
    list = [spotNode]
    isRoot = True

    while len(list) != 0:
        node = list.pop()
        tempCoor = node.split(",")
        xCoordinate = int(tempCoor[0])
        yCoordinate = int(tempCoor[1])


        if not graph.isLessThanParent(xCoordinate,yCoordinate) and not isRoot:
            continue

        #child value is lower so we check coor if on edge
        if graph.isOnEdge(xCoordinate,yCoordinate):
            graph.printParentValMatrix()

            graph.printPath(x,y,xCoordinate,yCoordinate)
        graph.populate(xCoordinate,yCoordinate,list, True, isRoot)
        isRoot = False

def bfs(graph,x,y): #depth first search
    if graph.matrixIsEmpty(): #check if graph empty
        print("graph is empty")
        return
    if graph.isOutOfRange(x,y): #check if invalid spot coor
        print("invalid spot")
        return
    if graph.isOnEdge(x,y):#if spot on edge return true
        return True

    spotNode = str(x) + "," + str(y) #make root node from spot
    graph.parentValMatrix[y][x] = spotNode
    list = [spotNode] #dps makes use of a stack
    isRoot = True

    while len(list) != 0:
        node = list.pop()
        tempCoor = node.split(",")
        xCoordinate = int(tempCoor[0])
        yCoordinate = int(tempCoor[1])#set to -1, -1 next time for isroot
        if not graph.isLessThanParent(xCoordinate,yCoordinate) and not isRoot: #ignore if child value is greater than parent
            continue
        isRoot = False
        #child value is lower so we check coor if on edge
        if graph.isOnEdge(xCoordinate,yCoordinate):
            graph.printParentValMatrix()
            graph.printPath(x,y,xCoordinate,yCoordinate)

        graph.populate(xCoordinate,yCoordinate,list, False,isRoot)

print(bfs(myGraph,2,2))
