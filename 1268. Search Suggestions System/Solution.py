class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        N = len(searchWord)
        res = []
        for i in range(N):
            print(searchWord[:i+1])
            cur_word = searchWord[:i+1]
            res.append([])
            for product in products:
                if product.startswith(cur_word):
                    res[i].append(product)
                res[i].sort()
                res[i] = res[i][:3]
                
        return res
