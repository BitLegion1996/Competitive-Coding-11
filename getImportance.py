class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        '''
        Create a hash map of employee id : emplyee class 
        Do BFS and compute the importance. 
        T = O(N*V)
        S = O(N)
        '''
        emap = {e.id: e for e in employees}
        q = [] 
        q.append( emap[id] )
        visited = [] 
        visited.append(id)
        importance = 0 
        while q:
            curr = q.pop(0)
            importance += curr.importance
            for subordinate in curr.subordinates:
                if subordinate not in visited:
                    visited.append( subordinate )
                    q.append( emap[subordinate]  )
        return importance
    
