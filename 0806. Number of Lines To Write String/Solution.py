class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        def get_width(byte):
            return widths[int(ord(byte) - 97)]
        
        cur_width = 0
        lines = 1
        
        for char in s:
            if (cur_width + get_width(char)) <= 100:
                cur_width += get_width(char)
            else:                
                lines += 1
                cur_width = 0
                cur_width += get_width(char)
        
        return [lines, cur_width]
        
