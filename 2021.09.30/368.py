class Solution:
    def __init__(self):
        self.answer = []
    
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        
        tree = {}
        for num in nums:
            self.insert(tree, num)
        
        depth = self.return_depth(tree)
        
        answer = []
        return_val = self.dfs(tree, answer, depth)
        
        return return_val
    
    def insert(self, tree, num):
        isDiv = False
        for key in tree:
            if key % num == 0:
                self.insert(tree[key], num)
                isDiv = True
        if not isDiv:
            tree[num] = {}
            
    def return_depth(self, node):
        if not node:
            return 0
        depth_list = []
        for key in node:
            depth_list.append(self.return_depth(node[key]))
        return max(depth_list) + 1
    
    def dfs(self, node, answer, depth):
        if len(answer) == depth:
            self.answer = answer
            return answer
        
        for key in node:
            answer.append(key)
            return_val = self.dfs(node[key], answer, depth)
            if return_val:
                return return_val
            answer.pop()
        return False
            