class Solution:
    def orangesRotting(self, matrix: List[List[int]]) -> int:

        rows =  len(matrix)
        cols =  len(matrix[0])
        
        rotten = []
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                        fresh+=1
                elif matrix[i][j] == 2:
                    rotten.append([i,j])
                  
        
        if not rotten and not fresh:
         
            return 0
        if  not rotten and fresh:
            return -1
     
        mins = 0

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while rotten:
                cnt = len(rotten)
                for i in range(cnt):
                    i,j = rotten.pop(0)
                    for d in directions:
                        ni = i+d[0]
                        nj = j+d[1]
                        if ni >= 0 and nj >= 0 and ni < rows and nj < cols and matrix[ni][nj] == 1:
                            matrix[ni][nj] = 2
                            rotten.append([ni,nj])
                            fresh -= 1
                mins += 1
        return mins-1 if fresh == 0 else -1
            