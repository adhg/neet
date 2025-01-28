 

class Solution(object):
    def solve(self, my_list):
        
        res = []
        combo = []
        def backtrack(i, combo):
            if i>=len(my_list):
                return
            if len(combo)==len(my_list):
                res.append(combo[:])
                return
            

            for ix in range(len(my_list)):
                if not my_list[ix] in combo: #CANT HAVE SAME NUMBER
                    combo.append(my_list[ix])
                    backtrack(ix,combo)
                    combo.pop() 

        backtrack(0,combo)
        return res
        


if __name__=='__main__':
    print ("start...")
    
    s = Solution()

    my_list = [1,2,3,4]   
    res = s.solve(my_list)
    for r in res:
        print (r)
    
    print ("END")