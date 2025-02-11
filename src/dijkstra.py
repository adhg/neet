import heapq
from collections import defaultdict

class Solution:
    
    def shortestPath(self, n, edges, src):
                 
        adj = defaultdict(list)
        for s, dest, distance in edges:
            adj[s].append( [dest, distance] ) #KEY src, Value--> [ [dest, distance]...[] ]
            
        shortest = {}
        minHeap = [ [0,src] ] # DISTANCE, SOURCE
        
        while minHeap:
            
            w1, n1 = heapq.heappop(minHeap)
            
            if n1 in shortest:
                continue
            shortest[n1]=w1
            
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    minHeap.append( [w1+w2, n2] )
            heapq.heapify(minHeap)
                
        #if no connection from/to use -1
        for i in range(n):
            if i not in shortest:
                shortest[i]=-1
    
        return shortest
        

if __name__=='__main__':
    print ("start...")
    
    n = 5
    
    #Src Des Weight 
    edges = [
                [0,1,10], 
                [0,2,3], [1,3,2],
                [2,1,4], [2,3,8],
                [2,4,2], [3,4,5]
            ]
    src = 0
    s = Solution()
    r = s.shortestPath(n,edges, src)
    print (r)
        
    print ("\nEND")