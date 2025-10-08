from idlelib.pyparse import trans


def transpose(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):

        new_matrix.append([ matrix[j][i] for j in range(len(matrix))    ])
    return new_matrix

def determinant(matrix):
    det = 0
    n = len(matrix)
    if n == 2:      #handles case of 2 x 2
        det = matrix[0][0] * matrix[1][1] - matrix[1][0]*matrix[0][1]
    if n>2:

        running_det = 0      #running total of determinant as a sum of parts
        for m in range(n):          #we create minor matrices for each column
            minor = [ [] for p in range(n-1)   ]         # minor matrices are n-1 x n-1
            for l in range(n-1):                         # we want to fill all n-1 rows
                for i in range(m):
                  minor[l].append(matrix[l+1][i])      # fill with values left of the split
                for j in range(n-1-m):
                    minor[l].append(matrix[l+1][j+1+m])   #fill with values right of the split
            running_det +=    (-1)**m * matrix[0][m] * determinant(minor)      #calculate how minor impacts on total determinant ( recursive )
        det = running_det
    return det

def inverse(matrix):
    inverse_mat = []
    n = len(matrix)
    det = determinant(matrix)
    if det == 0:
        print('Matrix is non-invertible')
    if n == 2:
        inverse_mat =  [  [matrix[1,1]/det       ,-matrix[0,1]/det]      ,  [-matrix[1][0]/det        ,matrix[0][0]/det]    ]
    if n > 2:
        inverse_mat = []
        untransposed_inverse_mat = [  [ [] for x in range(n)     ]   for y in range(n)    ]
        for p in range(n):
            for q in range(n):
                minor = [[] for p in range(n - 1)]  # minor matrices are n-1 x n-1
                for a in range(p):  # above the split
                    for i in range(q):    # left of split
                        minor[a].append(matrix[a][i])
                    for j in range(n - 1 - q):   #right of split
                        minor[a].append(matrix[a][j + 1 + q])
                for b in range(n-1-p):   #below split
                    for i in range(q):   #left of split
                        minor[b+p].append(matrix[b + 1 + p][i])
                    for j in range(n - 1 - q):   #right of split
                        minor[b+p].append(matrix[b+1+p][j + 1 + q])
                untransposed_inverse_mat[p][q] = determinant(minor) * (-1)**(p+q)    / det    #we go straight from matrix of minors --> cofactors matrix --> adjoint --> inverse like this as a partwise solution is preferable to a stepwise
        inverse_mat = transpose(untransposed_inverse_mat)
    return inverse_mat


