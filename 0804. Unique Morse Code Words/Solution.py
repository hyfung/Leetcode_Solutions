class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # First we transform all words into morse code
        mapping = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        morse_codes = []
        for word in words:
            morsified = ""
            for char in word:
                # Ascii lookup
                # Using 0-25 a-z lookup table
                morsified += mapping[ord(char) - 97]
            morse_codes.append(morsified)
         
        # Then add it to a hashmap
        morse_set = set()
        for morse in morse_codes:
            morse_set.add(morse)
        
        # Then return number of keys
        return len(morse_set)
            
        
        
        
