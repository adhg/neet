from collections import deque

gate  = 0
wall = -1
empty = float('inf')
        
class Solution:
    
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        
        rows = len(rooms)
        colls = len(rooms[0])
        
        #identify the gates
        d_queue = deque()
        
        for r in range (rows):
            for c in range (colls):                
                value = rooms[r][c]
                if value==gate:
                    d_queue.append( (r,c,0) ) #adding only gates (distance is zero)
                
        #given the gates - calc the distance from each gate to the next cell
        directions = [(1,0),(0,1),(-1,0),(0,-1)] 
        while d_queue:
            dq_len = len(d_queue)
            for i in range(0,dq_len):
                r,c,distance = d_queue.popleft()
                                
                #move to each direction
                for d in directions:
                    cell_r = r+d[0]
                    cell_c = c+d[1]
                     
                    #out of boundries
                    if cell_r<0 or cell_r>=rows or cell_c<0 or cell_c>=colls:
                        continue
                                                            
                    #wall?
                    new_cell_value = rooms[cell_r][cell_c]
                    if new_cell_value==wall:
                        continue
                    
                    #gate?
                    if new_cell_value==gate:
                        continue
                    
                    #has distance and it's more than the current distance + 1
                    if new_cell_value!=empty and new_cell_value<=distance+1:
                        continue

                    d_queue.append( (cell_r, cell_c, distance+1) ) 
                    rooms[cell_r][cell_c]=distance+1 #update new distance 
                             
        return rooms
    


if __name__=='__main__':
    print ("Start...")
    
    

    
    rooms = [
                [empty,wall,gate,empty],
                [empty,empty,empty,wall],
                [empty,wall,empty,wall],
                [gate,wall,empty,empty],        
    ]
    
    s = Solution()
    res = s.wallsAndGates(rooms)
    
    print ('resutls...')
    for r in res:
        print (r)
    
    print ("END")