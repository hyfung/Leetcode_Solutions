class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # If the input list is empty then return empty string
        if strs == []:
            return ""
        
        # Setup a placeholder for return value
        LCP = ""

        # Get the length of shortest string as for-loop upperbound
        max_len = min([len(x) for x in strs])
        
        # Loop through the strings, one character at a time
        for i in range(max_len):
            # Use Set() to check if there is only 1 character
            if len(set([x[i] for x in strs])) == 1:
                LCP += strs[0][i]
            # No more common prefix, terminate the loop
            else:
                break
        
        return LCP
        
