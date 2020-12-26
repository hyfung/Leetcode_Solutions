class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def is_data(b):
            return b & 0b10000000 == 0b10000000
        
        def num_byte(b):
            if b & 0b11110000 == 0b11110000:
                return 4
            elif b & 0b11100000 == 0b11100000:
                return 3
            elif b & 0b11000000 == 0b11000000:
                return 2
            elif b & 0b10000000 == 0b10000000:
                return 0
            else:
                return 1
            
            
        skip = 0
        try:
            for i,v in enumerate(data):
                if skip:
                    skip -= 1
                    continue
                
                if v & 0b11111000 == 0b11111000:
                    # Malformed character
                    return False
                
                elif num_byte(v) == 1:
                    # We hit 1-byte data and we don't expect cont. byte
                    continue
                elif num_byte(v) == 2:
                    # Check for next byte
                    if not is_data(data[i+1]):
                        print(2)
                        return False
                    skip = 1
                elif num_byte(v) == 3:
                    if not is_data(data[i+1]) or not is_data(data[i+2]):
                        print(3)
                        return False
                    skip = 2
                elif num_byte(v) == 4:
                    if not is_data(data[i+1]) or not is_data(data[i+2]) or not is_data(data[i+3]):
                        print(i, 3)
                        return False
                    skip = 3
                else:
                    print(4)
                    return False

            return True
        
        except:
            return False

            
        
