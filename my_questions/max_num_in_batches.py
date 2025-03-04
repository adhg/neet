import heapq

class Solution:
    
    def max_results(self, all_lists, k=10):
        
        min_heap = []

        for lst in all_lists:
            for num in lst:
                heapq.heappush(min_heap, num)  # Push number into heap
                if len(min_heap) > k:
                    heapq.heappop(min_heap)  #Remove smallest to keep size 10 (o(logn))
 
        top_10 = sorted(min_heap, reverse=True) 
        return top_10
    
if __name__=='__main__':
    print ("START...")
    
    n1 = [88, 56, 55, 43, 22, 10, 6, 5, 4, 4]
    n2 = [2038, 135, 51, 40, 11, 11, 6, 5, 1, 1]
    n3 = [999, 876, 500, 300, 250, 100, 50, 25, 10, 5]
    n4 = [1500, 900, 850, 800, 750, 600, 500, 400, 300, 200]
    n5 = [1800, 1200, 1100, 1000, 900, 800, 700, 600, 500, 400]
    n6 = [95, 85, 75, 65, 55, 45, 35, 25, 15, 5]
    n7 = [1000, 950, 900, 850, 800, 750, 700, 650, 600, 550]

    ns = [n1,n2,n3,n4,n5,n6,n7]
      
    s = Solution()
    top_10 = s.max_results(ns, k=10)
    print ("RES:=",top_10)
    print ("END")
