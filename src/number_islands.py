class Solution(object):
    
    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(r,c):
                        
            #out of bounds
            if r>=rows or c>=cols or r<0 or c<0:
                return False
            
            pos = (r,c)     
            print (pos,grid[r][c])
            
            if pos in visited: #visited?
                return False
            if grid[r][c]=="0": # not an island
                visited.add(pos)
                return False
                        
            #found an island - mark the nearby islands
            visited.add(pos)            
            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r-1,c)
                        
            return True
        
        visited = set()
        counter = 0
        for r in range(0,rows):
            for c in range (0,cols):
                
                islands = dfs(r,c)
                print ("__________________")
                if islands:
                    counter+=1
        
        return counter
        

if __name__=='__main__':
    print ("START...")
        
    grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
    ]
    
    s = Solution()
    num = s.numIslands(grid)
    print ("result:=",num)
    
    print ("END")
        