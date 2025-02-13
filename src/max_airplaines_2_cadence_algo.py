import heapq

class Solution:
    def max_airplanes(self, airplanes):
        if not airplanes:
            return 0        
        
        events = []
        for f in airplanes:
            events.append( (f[0],1) ) # departure (in air)
            events.append( (f[1],-1)) #landed
        
        events.sort(key=lambda x: (x[0],x[1]))
        
        counter = 0 
        max_airplanes = 0
        for e in events:
            status = e[1]
            counter += status
            max_airplanes = max(max_airplanes, counter)
        
        return max_airplanes


# Test
if __name__ == '__main__':
    print("Start...")
    
    airplanes = [[4, 8], [2, 5], [17, 20], [10, 21], [9, 18], [11, 12], [11, 13], ,[10,13]]
    s = Solution()
    p = s.max_airplanes(airplanes)
    
    print("Max airplanes in the air at the same time:", p)
    print("\nEND")
