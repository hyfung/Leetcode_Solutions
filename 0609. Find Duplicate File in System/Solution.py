class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashmap = dict()
        
        # Try to parse the path
        for path in paths:
            p = path.split()
            for p_ in p[1:]:
                dir_file = (p[0]+"/"+p_).rstrip(")").split("(")
                print(dir_file)
                
                if dir_file[1] not in hashmap:
                    hashmap[dir_file[1]] = [dir_file[0]]
                else:
                    hashmap[dir_file[1]] += [dir_file[0]]
        
        print(hashmap)
        
        res = []
        
        for k,v in hashmap.items():
            if len(v) > 1:
                res.append(v)
                
        return res
        
        
