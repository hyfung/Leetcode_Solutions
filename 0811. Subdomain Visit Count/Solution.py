class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        hashmap = dict()
        res = []
        
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(' ')
            count = int(count)
            
            domains = [domain]
            
            while '.' in domain:
                domain = domain[domain.index('.')+1:]
                domains.append(domain)
            
            for domain in domains:           
                if domain not in hashmap:
                    hashmap[domain] = count
                else:
                    hashmap[domain] += count
            
        for k,v in hashmap.items():
            res.append(f"{v} {k}")
        
        return res
