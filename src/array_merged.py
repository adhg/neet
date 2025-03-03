
class Solution(object):
    def merge(self, nums1, m, nums2, n):                                                          
        last = m + n - 1
        p1 = m - 1
        p2 = n - 1
        
        #Merge
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[last] = nums1[p1]
                p1 -= 1
            else: #swap
                nums1[last] = nums2[p2]
                p2 -= 1
            last -= 1
        
        #leftovers
        while p2 >= 0:
            nums1[last] = nums2[p2]
            p2 -= 1
            last -= 1

        
        
                    
if __name__=='__main__':
    print ("start...")
    
          
    s = Solution()
    nums1 = [0,0,0,0,0]
    m = 0
    nums2 = [1,2,3,4,5]
    n = 5
    s.merge(nums1, m, nums2, n)
    print (nums1)
    
    print ("END")