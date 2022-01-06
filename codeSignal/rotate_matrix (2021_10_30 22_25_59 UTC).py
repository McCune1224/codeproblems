def rotateMatrix(matrix):
    N = len(matrix)
    #transpose
    for i in range(N):
        for j in range(i,N):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    #flip
    for i in range(N//2):
        for j in range(N):
            matrix[j][i], matrix[j][N-1-i] = matrix[j][N-1-i], matrix[j][i]

def print_matrix(matrix):
    mat_str = ""
    for _, li in enumerate(matrix):
        for _, ele in enumerate(li):
            mat_str += str(ele) + " "
        mat_str += "\n"
    print(mat_str)



if __name__ == "__main__":
    test_case = [[1,2,3],[4,5,6],[7,8,9]]
    print_matrix(test_case)
    rotateMatrix(test_case)
    print_matrix(test_case)
