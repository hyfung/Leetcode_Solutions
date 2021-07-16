class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Parse the version number
        version1 = [int(x) for x in version1.split(".")]
        version2 = [int(x) for x in version2.split(".")]
        
        # Calculate length difference for padding
        len_v1 = len(version1)
        len_v2 = len(version2)
        
        # Padding the list
        if len_v1 > len_v2:
            version2 += [0] * abs(len_v1 - len_v2)
        if len_v2 > len_v1:
            version1 += [0] * abs(len_v1 - len_v2)        
        
        for i in range(len(version1)):
            if version1[i] > version2[i]:
                return 1
            if version1[i] < version2[i]:
                return -1
        
        return 0
    
