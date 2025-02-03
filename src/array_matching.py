
class Solution(object):
    def stringMatching(self, words):
                
        words.sort(key = lambda x: len(x))
        res = []
        for i,w in enumerate(words):
            for x in range (i+1, len(words)):
                my_word = words[x]
                if w in my_word:
                    res.append(w)
                    break                                    
        return res
                    
if __name__=='__main__':
    print ("start...")
    
    words = ["leetcoder","leetcode","od","hamlet","am"]#["mass","as","hero","superhero"]
    
    s = Solution()
    res = s.stringMatching(words)
    print (res)
    
    print ("END")