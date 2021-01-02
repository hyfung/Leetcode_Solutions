class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        A = 0
        B = 0
        
        secret_d = dict()
        guess_d = dict()
        
        # Construct a hashmap
        for i in range(len(secret)):
            if secret[i] in secret_d:
                secret_d[secret[i]] += 1
            else:
                secret_d[secret[i]] = 1
            
            if guess[i] in guess_d:
                guess_d[guess[i]] += 1
            else:
                guess_d[guess[i]] = 1
        
        # First check for bulls, then deduct from dictionary
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
                secret_d[secret[i]] -= 1
                guess_d[secret[i]] -= 1
                
        # Check for cows from remaining guess-secret pair
        for k in guess_d.keys():
            if k in secret_d:
                B += min(secret_d[k], guess_d[k])
        
        return str(A) + "A" + str(B) + "B"
