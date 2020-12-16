class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = dict()
        
        for word in strs:
            if "".join(sorted([char for char in word])) not in dictionary:
                dictionary["".join(sorted([char for char in word]))] = [word]
            else:
                dictionary["".join(sorted([char for char in word]))].append(word)
        
        print(dictionary)
        
        return dictionary.values()
