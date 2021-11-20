def matrixElementSum(matrix):
    ignore_index = []
    matrix_sum = 0
    for oIdx, curr_list in enumerate(matrix):
        for iIdx, list_element in enumerate(curr_list): 
            if list_element == 0:
                ignore_index.append(iIdx)
            if iIdx in ignore_index:
                continue
            else:
                matrix_sum = matrix_sum + list_element
    print(matrix_sum)


if __name__ == "__main__":
    test_matrix = [[0, 1, 1, 2],
                   [0, 5, 0, 0],
                   [2, 0, 3, 3]]

    matrixElementSum(matrix=test_matrix)
