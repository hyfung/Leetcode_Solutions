class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a_real, a_img = a.split("+")
        b_real, b_img = b.split("+")
        
        a_comp = complex(int(a_real), int(a_img.rstrip('i')))
        b_comp = complex(int(b_real), int(b_img.rstrip('i')))

        c = a_comp * b_comp        
        
        return str(int(c.real))+"+"+str(int(c.imag))+"i"
        
