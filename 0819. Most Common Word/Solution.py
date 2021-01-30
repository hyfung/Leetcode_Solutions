class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.replace(';', ' ')
        paragraph = paragraph.replace(':', ' ')
        paragraph = paragraph.replace('?', ' ')
        paragraph = paragraph.replace('.', ' ')
        paragraph = paragraph.replace('\'', ' ')
        paragraph = paragraph.replace('!', ' ')
        paragraph = paragraph.replace(',', ' ').lower()
        
        paragraphList = paragraph.split(' ')
        d = dict()
        
        for word in paragraphList:
            if word not in banned and word is not '':
                if word not in d:
                    d[word] = 1
                else:
                    d[word] += 1
        
        l = sorted(list(d.items()), key=lambda x: x[1])
        return l[-1][0]
        
        
