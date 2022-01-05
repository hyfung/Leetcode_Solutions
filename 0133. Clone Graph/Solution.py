"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return
        
        queue = []
        edges = []
        
        queue.append(node)
        
        visited = set()
        values = set()
        
        while queue:
            currNode = queue.pop()
            visited.add(currNode)
            values.add(currNode.val)
            for node in currNode.neighbors:
                if node not in visited:
                    queue.append(node)
                    print(currNode.val, node.val)
                    edges.append((currNode.val, node.val))
        
        print(edges)
        print(values)
        
        newNodes = dict()
        for v in values:
            newNodes[v] = Node(v)         
        
        for edge in edges:
            newNodes[edge[0]].neighbors.append(newNodes[edge[1]])
            newNodes[edge[1]].neighbors.append(newNodes[edge[0]])
        
        for k in newNodes.keys():
            return newNodes[k]
        
        
