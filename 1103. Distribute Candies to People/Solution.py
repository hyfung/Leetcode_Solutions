class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        lCandies = [0] * num_people
        turn = 1
        counter = 0
        
        while candies:
            if candies >= turn:
                lCandies[counter] += turn
                candies -= turn
                counter += 1
                turn += 1
                counter %= num_people
            else:
                lCandies[counter] += candies
                break
                
        return lCandies
        
