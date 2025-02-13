import heapq

class Solution:
    def max_airplanes(self, airplanes):
        if not airplanes:
            return 0

        # Step 1: Sort by departure time
        airplanes.sort(key=lambda x: x[0])
        print (airplanes)

        # Min-heap to track landing times
        q = []
        max_airplane = 0

        for start, end in airplanes:
            # Step 2: Remove all planes that have already landed
            while q:
                earliest_landing = q[0]  # Check the earliest landing time
                if earliest_landing>start:
                    break  # DO NOT REMOVE AND EXIT! this airplane is in AIR 
                heapq.heappop(q)  # Remove the landed plane (becuase it )
            
            # Step 3: Add the new flight's landing time (fixed placement)
            heapq.heappush(q, end)

            # Step 4: Track max number of planes in the air
            max_airplane = max(max_airplane, len(q))

        return max_airplane


# Test
if __name__ == '__main__':
    print("Start...")
    
    airplanes = [[4, 8], [2, 5], [17, 20], [10, 21], [9, 18], [11, 12], [11, 13], [10,13]]
    s = Solution()
    p = s.max_airplanes(airplanes)
    
    print("Max airplanes in the air at the same time:", p)
    print("\nEND")
