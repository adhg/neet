
class Solution:
    def countComponents(self, edges):
        def find(n1): # find root parent
            if n1 != child_parent[n1]:
                child_parent[n1] = find(child_parent[n1])
            return child_parent[n1]

        def union(n1, n2): # find root parent of each node
            p1 = find(n1)
            p2 = find(n2)
            if p1 == p2:
                return 0 # no union to perform
            child_parent[p1] = p2 # new Parent for p2
            return 1

        # step 1: build a child_parent dictionary where each child IS the parent (for now)
        my_set = set()
        for e in edges:
            my_set.add(e[0])
            my_set.add(e[1])

        child_parent = {i: i for i in my_set} # child_parent = {*#child, V=parent} 

        # step 2: assume all links are detached, if we find a union - decrement a link
        res = len(child_parent)
        for n1, n2 in edges:
            v = union(n1, n2)
            res -= v

        return res

if __name__ == "__main__":
    print("Start ...")
    edges = [['A', 'B'], ['I', 'Z'], ['M', 'N'], ['C', 'B'], ['J','Q'], ['B', 'Q'], ['V', 'T']]
    s = Solution()
    counter = s.countComponents(edges)
    print("counter =", counter)
    print("END")