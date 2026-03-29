class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)-1
        while l<=r:
            m=l+(r-l)//2
            if matrix[m][0]<=target and matrix[m][len(matrix[m])-1]>=target:
                b=0
                j=len(matrix[m])-1
                while b<=j:
                    k=b+(j-b)//2
                    if matrix[m][k]<target:
                        b=k+1
                    elif matrix[m][k]>target:
                        j=k-1
                    else:
                        return True
                return False

            if matrix[m][0]>target:
                r=m-1
            elif matrix[m][len(matrix[m])-1]<target:
                l=m+1
        return False