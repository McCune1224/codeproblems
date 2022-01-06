class Solution:
    def rotate(self, matrix: list[list[int]]) -> None: 
        #Length of the Matrix
        n = len(matrix[0])
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i, e in enumerate(matrix):
            #Flip First (123) -> (321)
            matrix[i] = matrix[i][::-1]




if __name__ == '__main__':
    t1 = [[1,2,3],[4,5,6],[7,8,9]]
    s = Solution()
    s.rotate(t1)
