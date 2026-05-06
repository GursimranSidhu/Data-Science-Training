class Solution:
    def searchMatrix(self, matrix, target):
        m=len(matrix)
        n=len(matrix[0])
        
        row=0
        col=n-1

        while row<m and col>=0:
            if matrix[row][col]==target:
                return True
            
            if matrix[row][col]>target:
                col-=1
                
            if matrix[row][col]<target:
                row+=1

        return False

if __name__ == "__main__":
    sol = Solution()
    
    # Input rows and columns
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))
    
    matrix = []
    print("Enter the matrix row-wise:")
    
    for i in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    target = int(input("Enter target value: "))
    
    result = sol.searchMatrix(matrix, target)
    
    print("Output:", result)