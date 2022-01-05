class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        # Convert into adjacency list
        
        if n == 1:
            return True
        
        adjList = dict()
        
        for edge in edges:
            if edge[0] not in adjList:
                adjList[edge[0]] = [edge[1]]
            else:
                adjList[edge[0]].append(edge[1])
                
            if edge[1] not in adjList:
                adjList[edge[1]] = [edge[0]]
            else:
                adjList[edge[1]].append(edge[0])
                
        visited = set()
        
        unvisited = list(adjList.keys())
        
        if start not in adjList.keys() or end not in adjList.keys():
            return False
        
        queue = []
        
        queue.append(start)
        
        while queue:
            currNode = queue.pop()
            visited.add(currNode)
            
            if currNode == end:
                return True
            
            for i in adjList[currNode]:
                if i not in visited:
                    queue.append(i)
            
        
        return False
            
