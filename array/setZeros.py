def setZerosoo(matrix):
    if matrix == None or len(matrix) == 0:
        return
    m = len(matrix)
    n = len(matrix[0])
    x,y = -1,-1
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                if x == -1 and y == -1:
                    x = i
                    y = j
                else:
                    matrix[x][j] = 0
                    matrix[i][y] = 0

    if x == -1 or y == -1:
        return

    for i in range(m):
        for j in range(n):
            print(matrix[1][0])
            # if matrix[x][j] == 0:#or matrix[i][y] == 0:
            #     matrix[i][j] = 0
            if matrix[i][y] == 0:
                matrix[i][j] = 0
    return matrix

def setZeros(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """

    idx = []
    for i in range(len(matrix)):
        if 0 in matrix[i]:
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    idx.append(j)
            matrix[i] = [0 for el in matrix[i]]
    setColToZero(matrix, idx)

    return matrix

def setColToZero(matrix,idx):
    for col in idx:
        for i in range(len(matrix)):
            matrix[i][col] = 0


matrix = [[0,1,3,4],[5,6,1,8],[9,10,11,12]]
print("inital:",matrix)
print("setZeros:",setZerosoo(matrix))
