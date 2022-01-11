class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        
        """
        while len(asteroids) > 0:
            if mass >= asteroids[0]:
                mass += asteroids.pop(0)
            else:
                return False
        
        return True
        """
        
        
        """
        for a in asteroids:
            if mass >= a:
                mass += a
            else:
                return False
            
        return True
        """
        
        for i in range(len(asteroids)):
            if mass >= asteroids[i]:
                mass += asteroids[i]
            else:
                return False
        
        return True
        
