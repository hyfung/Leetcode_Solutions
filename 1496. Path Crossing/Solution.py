class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        x, y = 0, 0
        visited.add((x,y))
        
        for char in path:
            if char == 'N':
                y += 1
                if (x,y) in visited:
                    return True
                visited.add((x,y))
            if char == 'S':
                y -= 1
                if (x,y) in visited:
                    return True
                visited.add((x,y))
            if char == 'W':
                x -= 1
                if (x,y) in visited:
                    return True
                visited.add((x,y))
            if char == 'E':
                x += 1
                if (x,y) in visited:
                    return True
                visited.add((x,y))
            
        return False
                
        
