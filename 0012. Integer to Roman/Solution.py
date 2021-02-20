class Solution:
    def intToRoman(self, num: int) -> str:
        sRet = ""
        
        thousand = {3000: "MMM", 2000: "MM", 1000: "M", 0:""}
        hundred = {900:"CM", 800:"DCCC", 700:"DCC",600:"DC",500:"D",400:"CD",300:"CCC",200:"CC",100:"C", 0:""}
        ten = {90:"XC",80:"LXXX",70:"LXX",60:"LX",50:"L",40:"XL",30:"XXX",20:"XX",10:"X",0:""}
        digit = {9:"IX",8:"VIII",7:"VII",6:"VI",5:"V",4:"IV",3:"III",2:"II",1:"I",0:""}
        
        sRet += thousand[num // 1000 * 1000 ]
        sRet += hundred[num % 1000 // 100 * 100]
        sRet += ten[num % 100 // 10 * 10]
        sRet += digit[num % 10]
        return sRet
        
        
        
