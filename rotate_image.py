class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l,r = 0, len(matrix) - 1

        while l<r:
            for  i  in range(r-l):
                top, bottom = l,r

                #store topleft in temp
                topleft = matrix[top][l+i]

                #move bottomleft to topleft
                matrix[top][l+i] = matrix[bottom-i][l]

                #move bottomright to bottomleft
                matrix[bottom-i][l] = matrix[bottom][r -i]

                #move topright to bottom right
                matrix[bottom][r-i] = matrix[top+i][r]

                #move topleft to topright
                matrix[top+i][r] = topleft
            l=l+1
            r=r-1