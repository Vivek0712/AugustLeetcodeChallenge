# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    
 
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        levelmap = {}
        
        def vertical(root: TreeNode, x: int, y: int) -> None:
            if not root:
                return
            if x not in levelmap:
                levelmap[x] = []
            levelmap[x].append((y,root.val))
            vertical(root.left, x-1, y+1)
            vertical(root.right, x+1, y+1)
        
                               
        dfs(root, 0, 0)    
                                      
        res = []
        for key in sorted (levelmap.keys()) : 
                     
            listval = sorted(levelmap[key]) 
            temp = []
            for i in listval:
                temp.append(i[1])
            res.append(temp)
        return res
                